from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.forms import inlineformset_factory
from .models import Project, ProjectApproval, UserProfile, User
from .forms import ProjectForm, ApproverForm, CommentForm, ApproverFormSet, EditApproverFormSet
from django.utils import timezone


# ProjectList view for dashboard.html. Shows all the projects with related
# approvers


def ProjectList(request):
    projects = Project.objects.order_by('status','due')
    projectId = Project.objects.values_list('id')
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals
    }

    return render(request, 'dashboard.html', context)


# ProjectDetails view for project-details.html.
# Render all the details related to a project and its comments

class ProjectDetails(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Project.objects
        project = get_object_or_404(queryset, slug=slug)
        approvals = project.approvals.all()
        comments = project.comments.order_by("created_on")

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
        approvals = project.approvals.all()
        comments = project.comments.order_by("created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.save()
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
            project = form.save()
            approver_form = ApproverFormSet(request.POST, instance=project)
            if approver_form.is_valid():
                approver_form.save()
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
                return redirect('dashboard')
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
    return redirect('dashboard')

# view to delete approvers the projcts in the project-details template

# def DeleteApprover(request, projectApproval_id):
#     approver = get_object_or_404(ProjectApproval, id=projectApproval_id)
#     approver.delete()
#     return redirect('dashboard')


# view to delete projects the projcts in the project-details template


def DeleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('dashboard')


# view to complete the projcts in the project-details template


def CompleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.status = not 0
    project.save()
    return redirect('dashboard')


# ProjectList view for my-projects.html. Shows all the projects opened by the
# signed in user


def MyProjectList(request):
    user = request.user.id
    projects = Project.objects.filter(owner=user).order_by('status','due')
    projectId = Project.objects.values_list('id')
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals
    }

    return render(request, 'my-projects.html', context)


# MyApprovalsList view for my-approvals.html. Shows all the projects that the 
# logged in user needs to approve


def MyApprovalsList(request):
    user = request.user.id
    project = Project.objects.all()
    projects = Project.objects.distinct().filter(
        approvals__approver_id=user
        ).order_by(
            'due', 'status'
        )
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals

    }

    return render(request, 'my-approvals.html', context)