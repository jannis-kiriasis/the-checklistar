from django.contrib import admin
from .models import Project, ProjectApprover, UserProfile

# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectApprover)
admin.site.register(UserProfile)