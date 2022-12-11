from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    get_list_or_404,
)
from .forms import (
    ProjectForm,
    ApproverForm,
    CommentForm,
    approver_formset,
    edit_approver_formset,
)
from django.views import generic, View
from django.forms import inlineformset_factory
from .models import Project, ProjectApproval, UserProfile, User
from django.utils import timezone
from notification.utilities import create_notification
from django.contrib import messages


def project_list(request):
    """
    project_list view for dashboard.html.
    Shows all the projects with related approvers.
    """
    user = request.user
    projects = Project.objects.order_by('-date_created')
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals,
        'user': user,
        'page_title': 'Dashboard',
        'project-details': 'project-details'
    }

    return render(request, 'dashboard.html', context)


def comment_form_is_valid(comment_form, request, project):
    """
    Check if comment form is valid. If so, add the comment, send a feedback
    and send a notification.
    """
    # If comment form is valid get user email and username
    # and save the data.
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.project = project
        comment.save()
        messages.success(request, 'You have commented successfully.')

        # I want to send a notification to the project owner and the
        # approvers depending on who has commented on the project.
        # If an approver has commented, the owner gets a notification.
        # If the owner has commented, all the approvers get a notification.
        # If someone else commented send a notification to the owner.
        project_approvals = ProjectApproval.objects.all()
        approver_list = get_list_or_404(
            project_approvals, project=project
            )

        # Check who is logged in. If it is the owner who commented, send a
        # notification to the approvers. Else send a notification to the
        # project owner.
        if request.user == project.owner:
            for approver in approver_list:
                create_notification(
                    request,
                    approver.approver.user,
                    'comment',
                    extra_id=project.slug
                    )
        else:
            create_notification(
                request, project.owner,
                'comment',
                extra_id=project.slug
                )
    else:
        comment_form = CommentForm()


# project_details view for project-details.html.
# Render all the details related to a project and its comments

def project_details(request, slug):
    """
    project_details view for project-details.html.
    Render all the details related to a project and its comments.
    """
    # Get project, approvals and comments.
    queryset = Project.objects
    project = get_object_or_404(queryset, slug=slug)
    approvals = project.approvals.order_by('created_on')
    comments = project.comments.order_by('-created_on')

    # Check if the request is a GET or a POST request.
    if request.method == 'GET':
        # If the request is a GET request, render the project-details.html
        # template with the project, approvals, comment form, and comments.
        return render(
            request,
            'project-details.html',
            {
                'project': project,
                'approvals': approvals,
                'comment_form': CommentForm,
                'comments': comments,
                'page_title': 'Project details'
            },
        )
    else:
        # POST project, approvals, comments.
        queryset = Project.objects
        project = get_object_or_404(queryset, slug=slug)
        approvals = project.approvals.order_by('created_on')
        comments = project.comments.order_by('-created_on')

        comment_form = CommentForm(data=request.POST)

        # Call function to validate comment form
        comment_form_is_valid(comment_form, request, project)

        return render(
            request,
            'project-details.html',
            {
                'project': project,
                'approvals': approvals,
                'comment_form': CommentForm,
                'comments': comments,
            },
            )


def create_project(request):
    """
    View to create a project. Takes the form and formset check if they
    are valid and if so save the objects in the related models.

    Send a notification to the approvers to say they have been added to
    a project.

    If the project is created, send a feedback.
    """
    form = ProjectForm()
    approver_form = approver_formset(instance=Project())
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            approver_form = approver_formset(request.POST, instance=project)
            if approver_form.is_valid():
                form.save()
                approver_form.save()
                # Feedback
                messages.success(request, 'You have created a new project!')

                last_project = Project.objects.latest('date_created')
                approvals = ProjectApproval.objects.all()

                # Send a notification to the approvers. If there are not
                # approvers for the project, skip this without error.
                try:
                    approver = get_list_or_404(approvals, project=last_project)
                    if approver:
                        for approver in approver:
                            create_notification(
                                request,
                                approver.approver.user,
                                'added_approver',
                                extra_id=project.slug
                                )
                        return redirect('dashboard')
                except Exception:
                    return redirect('dashboard')
        else:
            print('form invalid')

    context = {
        'form': form,
        'formset': approver_form,
        'page_title': 'Create project'
    }
    return render(request, 'create-project.html', context)


def edit_project(request, project_id):
    """
    View to edit a project. Takes the form and formset check if they
    are valid and if so save the objects in the related models.

    If the project is updated, send a feedback.
    """
    project = get_object_or_404(Project, id=project_id)
    form = ProjectForm(instance=project)
    approver_form = edit_approver_formset(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            approver_form = edit_approver_formset(
                request.POST, instance=project
                )
            if approver_form.is_valid():
                approver_form.save()
                # Feedback
                messages.success(
                    request, 'Project details have been updated successfully.'
                    )
                return redirect('my-projects')
            else:
                print('Approver form is invalid')
                print(approver_form)
        else:
            print('form invalid')

    context = {
        'form': form,
        'approver_form': approver_form,
        'page_title': 'Edit project'
    }
    return render(request, 'edit-project.html', context)


def approve_project(request, projectApproval_id):
    """
    View to approve the projcts.

    If approved, send a feedback and a notification.
    """
    approver = get_object_or_404(ProjectApproval, id=projectApproval_id)
    approver.approved = not approver.approved
    approver.approval_date = timezone.now()
    approver.save()
    # Feedback
    messages.success(request, 'You have approved the project.')

    create_notification(
        request,
        approver.project.owner,
        'approval',
        extra_id=approver.project.slug
        )

    return redirect('my-approvals')


def delete_project(request, project_id):
    """
    View to delete projects.
    If project is deleted, send a feedback.
    """
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, 'The project has been deleted.')

    return redirect('my-projects')


def complete_project(request, project_id):
    """
    View to complete the projcts.
    If project is completed, send a feedback.
    """
    project = get_object_or_404(Project, id=project_id)
    project.status = not 0
    project.save()
    messages.success(request, 'The project has been completed!')

    return redirect('my-projects')


# project_list view for my-projects.html. Shows all the projects opened by the
# signed in user


def my_project_list(request):
    """
    View for my-projects page.

    Get all the projects where the owner is the logged in user and related
    approvals.
    """
    user = request.user.id
    all_projects = Project.objects.filter(owner=user).order_by('-id', 'due')
    projects = all_projects.filter(status=0)
    projects_completed = all_projects.filter(status=1)
    approvals = ProjectApproval.objects.all()

    context = {
        'projects': projects,
        'approvals': approvals,
        'projects_completed': projects_completed,
        'page_title': 'My projects'
    }

    return render(request, 'my-projects.html', context)


def my_approvals_list(request):
    """
    View for my-approvals page.

    Get all the projects where the approver is the logged in user.
    """
    user = request.user.id

    # Get projects where there is an approver matching the requesting user
    project_approver_is_user = Project.objects.distinct().filter(
        approvals__approver_id=user
        )

    # In project_approver_is_user get only projects with status=uncompleted and
    # order them
    projects = project_approver_is_user.filter(
        status=0).order_by('-due')

    # In projects get only the projects where the requesting user
    # hasn't approved yet
    project_to_approve = projects.filter(approvals__approved=False)

    project_approved = projects.filter(approvals__approved=True)

    # Get all approvals and order them
    approvals = ProjectApproval.objects.order_by(
            '-approval_due_by', 'approved'
        )
    context = {
        'projects': project_to_approve,
        'approvals': approvals,
        'project_approved': project_approved,
        'page_title': 'My approvals'

    }

    return render(request, 'my-approvals.html', context)


def error_404_view(request, exception):
    """View for 404 page."""
    context = {
        'page_title': '404'
    }
    return render(request, '404.html', context)


def error_500_view(request, exception=None):
    """View for 500 error."""
    def get(self, request):
        # Get the exception that caused the 500 error
        exception = request.exception

    context = {
        'page_title': '500',
        'exception': exception
    }
    return render(request, '500.html', context)
