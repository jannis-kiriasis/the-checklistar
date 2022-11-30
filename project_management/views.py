from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.forms import inlineformset_factory
from .models import Project, ProjectApproval, UserProfile, User
from .forms import ProjectForm, ApproverForm, CommentForm, ApproverFormSet


# ProjectList view for dashboard.html. Shows all the projects with related
# approvers


def ProjectList(request):
    projects = Project.objects.order_by('-date_created')
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
    approver = get_object_or_404(ProjectApproval, project_id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        approver_form = ApproverForm(request.POST, instance=approver)
        if form.is_valid():
            project = form.save()
            if approver_form.is_valid():
                approver = approver_form.save(commit=False)
                approver.project = project
                approver.save()
            return redirect('dashboard')
    form = ProjectForm(instance=project)
    approver_form = ApproverForm(instance=approver)
    context = {
        'form': form,
        'approver_form': approver_form
    }
    return render(request, 'edit-project.html', context)


# view to approve the projcts in the project-details template


def ApproveProject(request, projectApproval_id):
    approver = get_object_or_404(ProjectApproval, id=projectApproval_id)
    approver.approved = not approver.approved
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