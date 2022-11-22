from django.contrib import admin
from .models import Project, ProjectApproval, UserProfile

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectApproval)
admin.site.register(UserProfile)
