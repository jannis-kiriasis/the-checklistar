from django.contrib import admin
from .models import Project, ProjectApproval, UserProfile, Comment
from django_summernote.admin import SummernoteModelAdmin


class ApprovalInline(admin.TabularInline):
    model = ProjectApproval


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created', 'owner')
    list_display = ('title', 'owner', 'date_created', 'status')
    summernote_fields = ('description')
    inlines = [
        ApprovalInline
    ]


@admin.register(ProjectApproval)
class ProjectApprovalAdmin(SummernoteModelAdmin):

    list_filter = ('project', 'approver')
    list_display = ('id', 'project', 'approver', 'approved')
    actions = ['approve_projects']

    def approve_projects(self, request, queryset):
        queryset.update(approved=True)


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):

    list_filter = ('user', 'department')
    list_display = ('user', 'department')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'project', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'body')
