from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import generic, View
from django.forms import inlineformset_factory
from .models import Project, ProjectApproval, UserProfile, User
from .forms import ProjectForm, ApproverForm, CommentForm, ApproverFormSet, EditApproverFormSet
from django.utils import timezone
from notification.utilities import create_notification
from django.contrib import messages


# ProjectList view for dashboard.html. Shows all the projects with related
# approvers


def ProjectList(request):
    projects = Project.objects.order_by('-date_created')
    projectId = Project.objects.values_list('id')
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals,
        'page_title': 'All projects'
    }

    return render(request, 'dashboard.html', context)


# ProjectDetails view for project-details.html.
# Render all the details related to a project and its comments

class ProjectDetails(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Project.objects
        project = get_object_or_404(queryset, slug=slug)
        approvals = project.approvals.order_by("created_on")
        comments = project.comments.order_by("-created_on")

        return render(
            request,
            "project-details.html",
            {
                "project": project,
                "approvals": approvals,
                "comment_form": CommentForm(),
                "comments": comments,
            },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Project.objects
        project = get_object_or_404(queryset, slug=slug)
        approvals = project.approvals.order_by("created_on")
        comments = project.comments.order_by("-created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, 'You have commented successfully.')

            
            # get all approvers of this project for if statement
            project_approvals = ProjectApproval.objects.all()
            approver_list = get_list_or_404(project_approvals, project=project)

            # get logged in user for elif statement
            # project_approvals_by_user_id = ProjectApproval.objects.filter(approver_id=request.user.id)
            # approver = get_object_or_404(project_approvals_by_user_id, project=project)
    
            if request.user == project.owner:
                for approver in approver_list:
                    create_notification(request, approver.approver.user, 'comment', extra_id=project.slug)
            else:
                create_notification(request, project.owner, 'comment', extra_id=project.slug)

        else:
            comment_form = CommentForm()

        return render(
            request,
            "project-details.html",
            {
                "project": project,
                "approvals": approvals,
                "comment_form": CommentForm(),
                "comments": comments,
            },
            )


# View to create a project. Takes the form and formset  
# and save the inputs in the related modeles.


def CreateProject(request):
    form = ProjectForm()
    approver_form = ApproverFormSet(instance=Project())
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            approver_form = ApproverFormSet(request.POST, instance=project)
            if approver_form.is_valid():
                form.save()
                approver_form.save()

                messages.success(request, 'You have created a new project!')

                last_project = Project.objects.latest('date_created')
                approvals = ProjectApproval.objects.all()

                try:
                    approver = get_list_or_404(approvals, project=last_project)
                    if approver:
                        for approver in approver:
                            create_notification(request, approver.approver.user, 'added_approver', extra_id=project.slug)
                        return redirect('dashboard')
                except Exception:
                    return redirect('dashboard')
        else:
            print('form invalid')

    context = {
        'form': form,
        'formset': approver_form
    }
    return render(request, 'create-project.html', context)


# view to edit the projcts in the project-details template

def EditProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(instance=project)
    approver_form = EditApproverFormSet(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            approver_form = EditApproverFormSet(request.POST, instance=project)
            
            if approver_form.is_valid():
                approver_form.save()
                messages.success(
                    request, 'Project details have been updated successfully.'
                    )
                return redirect('my-projects')
            else:
                print('Approver form is invalid')
                print(approver_form)
        else:
            print('form invalid')

    context = {
        'form': form,
        'approver_form': approver_form
    }
    return render(request, 'edit-project.html', context)



# view to approve the projcts in the project-details template


def ApproveProject(request, projectApproval_id):
    approver = get_object_or_404(ProjectApproval, id=projectApproval_id)
    approver.approved = not approver.approved
    approver.approval_date = timezone.now()
    approver.save()
    messages.success(request, 'You have approved the project.')

    create_notification(request, approver.project.owner, 'approval', extra_id=approver.project.slug)

    return redirect('my-approvals')


# view to delete projects the projcts in the project-details template


def DeleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, 'The project has been deleted.')

    return redirect('my-projects')


# view to complete the projcts in the project-details template


def CompleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.status = not 0
    project.save()
    messages.success(request, 'The project has been completed!')

    return redirect('my-projects')


# ProjectList view for my-projects.html. Shows all the projects opened by the
# signed in user


def MyProjectList(request):
    user = request.user.id
    all_projects = Project.objects.filter(owner=user).order_by('-id', 'due')
    projects = all_projects.filter(status=0)
    projects_completed = all_projects.filter(status=1)
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals,
        'projects_completed': projects_completed
    }

    return render(request, 'my-projects.html', context)


# MyApprovalsList view for my-approvals.html. Shows all the projects that the 
# logged in user needs to approve


def MyApprovalsList(request):
    user = request.user.id

    # Get projects where there is an approver matching the requesting user
    project_approver_is_user = Project.objects.distinct().filter(
        approvals__approver_id=user
        )

    # In project_approver_is_user get only projects with status=uncompleted and 
    # order them
    projects = project_approver_is_user.filter(status=0).order_by(
        '-due'
        )

    # In projects get only the projects where the requesting user 
    # hasn't approved yet
    project_to_approve = projects.filter(approvals__approved=False)

    project_approved = projects.filter(approvals__approved=True)

    # Get all approvals and order them
    approvals = ProjectApproval.objects.order_by(
            '-approval_due_by', 'approved'
        )
    context = {
        'projects': project_to_approve,
        'approvals': approvals,
        'project_approved': project_approved

    }

    return render(request, 'my-approvals.html', context)
