import csv
from django.contrib import admin
from django.http import HttpResponse
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
    actions = ("export_as_csv",)

    # fuction to export list of projects from admin panel
    # from https://stackoverflow.com/questions/58921265/django-admin-download-data-as-csv


    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(ProjectApproval)
class ProjectApprovalAdmin(SummernoteModelAdmin):

    list_filter = ('project', 'approver')
    list_display = ('id', 'project', 'project_id', 'approver', 'approved')
    actions = ['approve_projects', "export_as_csv"]


    def approve_projects(self, request, queryset):
        queryset.update(approved=True)


    # fuction to export list of projects from admin panel
    # from https://stackoverflow.com/questions/58921265/django-admin-download-data-as-csv

    
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):

    list_filter = ('user', 'department')
    list_display = ('user', 'department')
  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'project', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'body')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email_address')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)