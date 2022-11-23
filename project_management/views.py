from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Project, ProjectApproval, UserProfile, User
from .forms import ProjectForm
# ProjectList view for dashboard.html. Shows all the projects with related
# approvers


class ProjectList(generic.ListView):
    model = Project()
    queryset = Project.objects.order_by('-date_created')
    template_name = 'dashboard.html'
    paginate_by = 20

    # def get_context_data(self, **kwargs):
    #     context = super(ProjectList, self).get_context_data(**kwargs)
    #     context['approval_list'] = ProjectApproval.objects.all()
    #     return context


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
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'create-project.html', context)