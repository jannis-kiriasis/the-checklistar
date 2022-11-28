from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Project, ProjectApproval, UserProfile, User
# from .forms import ProjectForm


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

        return render(
            request,
            "project-details.html",
            {
                "project": project,
                "approvals": approvals,
            }
            )


def CreateProject(request):
    users = User.objects.all()
    userProfile = UserProfile.objects.all()
    projectApprovers = ProjectApproval.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        owner = request.POST.get("owner")
        description = request.POST.get("description")
        document = request.POST.get("document")
        approvers = request.POST.get("approvers")
        Project.objects.create(
            title=title,
            owner=User,
            description=description,
            document=document,
            )

        ProjectApproval.objects.create(
            project=request.title,
            approver=approvers
        )
        return redirect('dashboard')

    context = {
        'users': users
    }

    return render(request, 'create-project.html', context)

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
#         'form': form
#     }
#     return render(request, 'create-project.html', context)