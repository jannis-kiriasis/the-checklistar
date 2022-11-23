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