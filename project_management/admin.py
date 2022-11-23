from django.contrib import admin
from .models import Project, ProjectApproval, UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created', 'owner')
    list_display = ('title', 'owner', 'date_created', 'status')
    summernote_fields = ('description')


@admin.register(ProjectApproval)
class ProjectApprovalAdmin(SummernoteModelAdmin):

    list_filter = ('project', 'approver', 'approver_department')
    list_display = ('id', 'project', 'approver', 'approver_department', 'approved')
    actions = ['approve_projects']

    def approve_projects(self, request, queryset):
        queryset.update(approved=True)


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):

    list_filter = ('user', 'department')
    list_display = ('user', 'department')
