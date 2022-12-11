import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Project, ProjectApproval, UserProfile, Comment
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password


class UserProfileInline(admin.TabularInline):
    """
    Add UserProfile data to User table in admin panel.
    """
    model = UserProfile


class ApprovalInline(admin.TabularInline):
    """
    Add ProjectApproval data to Project table in admin panel.
    """
    model = ProjectApproval


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    """
    Setup Project fields, filters, actions and inlines in admin panel.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created', 'owner')
    list_display = ('title', 'owner', 'date_created', 'status')
    inlines = [
        ApprovalInline
    ]
    actions = ('export_as_csv',)

    # fuction to export list of projects from admin panel
    # from
    # stackoverflow.com/questions/58921265/django-admin-download-data-as-csv

    def export_as_csv(self, request, queryset):
        """
        Export projects as csv.
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'
            ] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow(
                [getattr(obj, field) for field in field_names]
                )

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(ProjectApproval)
class ProjectApprovalAdmin(SummernoteModelAdmin):
    """
    Setup ProjectApproval fields, filters, actions and inlines in admin panel.
    """
    list_filter = ('project', 'approver')
    list_display = ('id', 'project', 'project_id', 'approver', 'approved')
    actions = ['approve_projects', 'export_as_csv']

    def approve_projects(self, request, queryset):
        """
        Approve projects from admin panel.
        """
        queryset.update(approved=True)

    # fuction to export list of project approvals from admin panel
    # from
    # stackoverflow.com/questions/58921265/django-admin-download-data-as-csv

    def export_as_csv(self, request, queryset):
        """
        Export project approvals as csv.
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'
            ] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow(
                [getattr(obj, field) for field in field_names]
                )

        return response

    export_as_csv.short_description = 'Export Selected'


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    """
    Setup filter and fields to display for UserProfile in admin panel.
    """
    list_filter = ('user', 'department')
    list_display = ('user', 'department')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Setup filter and fields to display for comments in admin panel.
    """
    list_display = ('name', 'body', 'project', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'body')


class UserAdmin(admin.ModelAdmin):
    """
    Setup fields to display and inlines for User in admin panel.
    """
    list_display = ('username', 'first_name', 'last_name')
    inlines = [UserProfileInline]

    # Hash the password before to save the User
    # or user login will fail
    def save_model(self, request, obj, form, change):
        """
        Get the password object, hash it and save it.
        """
        obj.password = make_password(form.cleaned_data['password'])
        obj.save()

# Unregister User because UserAdmin has been defined just above


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
