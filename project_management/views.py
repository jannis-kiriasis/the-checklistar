from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Project, ProjectApproval, UserProfile, User

# ProjectList view for dashboard.html. Shows all the projects with related
# approvers


class ProjectList(generic.ListView):
    model = ProjectApproval
    queryset = ProjectApproval.objects.order_by('-project')
    template_name = 'dashboard.html'
    paginate_by = 20


def CreateProject(request):
    options = User.objects.order_by('username')
    context = {}
    return render(request, "create-project.html", context)