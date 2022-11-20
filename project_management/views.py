from django.shortcuts import render 
from django.views import generic
from .models import Project, ProjectApprover

# Create your views here.

class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.order_by('-date_created')
    template_name = 'dashboard.html'
    paginate_by = 20

