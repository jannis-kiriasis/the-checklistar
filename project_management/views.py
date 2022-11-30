from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Project, ProjectApproval, UserProfile, User
from .forms import ProjectForm, ApproverForm, CommentForm


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


# class ProjectList(generic.ListView):
#     queryset = Project.objects.order_by('-date_created')
#     template_name = 'dashboard.html'
#     paginate_by = 20

#     def get_context_data(self, **kwargs):
#         context = super(ProjectList, self).get_context_data(**kwargs)
#         context['approval_list'] = ProjectApproval.objects.all()
#         return context


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
                "comments": comments
            }
            )


# def CreateProject(request):
#     users = User.objects.all()
#     userProfile = UserProfile.objects.all()
#     projectApprovers = ProjectApproval.objects.all()

#     if request.method == "POST":
#         title = request.POST.get("title")
#         owner = request.POST.get("owner")
#         description = request.POST.get("description")
#         document = request.POST.get("document")
#         approvers = request.POST.get("approvers")
#         Project.objects.create(
#             title=title,
#             owner=User,
#             description=description,
#             document=document,
#             )

#         ProjectApproval.objects.create(
#             project=request.title,
#             approver=approvers
#         )
#         return redirect('dashboard')

#     context = {
#         'users': users
#     }

#     return render(request, 'create-project.html', context)

# def CreateProject(request):
#     form = ProjectForm()
#     if request.method == "POST":
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#         else:
#             print('form invalid')
#     context = {
#         'form': form,
#     }
#     return render(request, 'create-project.html', context)

def CreateProject(request):
    form = ProjectForm()
    approver_form = ApproverForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        approver_form = ApproverForm(request.POST)
        if form.is_valid():
            project = form.save()
            if approver_form.is_valid():
                approver = approver_form.save(commit=False)
                approver.project = project
                approver.save()
            return redirect('dashboard')
        else:
            print('form invalid')
    context = {
        'form': form,
        'approver_form': approver_form
    }
    return render(request, 'create-project.html', context)


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


def ApproveProject(request, projectApproval_id):
    approver = get_object_or_404(ProjectApproval, id=projectApproval_id)
    approver.approved = not approver.approved
    approver.save()
    return redirect('dashboard')

def DeleteApprover(request, projectApproval_id):
    approver = get_object_or_404(ProjectApproval, id=projectApproval_id)
    approver.delete()
    return redirect('dashboard')

def DeleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('dashboard')