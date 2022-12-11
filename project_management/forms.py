from .models import Project, ProjectApproval, User, UserProfile, Comment
from django import forms
from django.forms import inlineformset_factory, widgets
from django.utils import timezone
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm


class ProjectForm(forms.ModelForm):
    """
    Create a project form.
    """
    class Meta:
        """
        Set create a project form model, fields, widgets.
        """
        model = Project
        fields = ['title', 'owner', 'description', 'document', 'due']
        widgets = {
            'due': widgets.DateInput(attrs={'type': 'date'})
        }

    def clean(self, view=None):
        """
        Evaluate whether the project form is called by the create_form view or
        by the edit_form view.

        If it is called by the create_form view, check that title is unique.
        If it isn't raise an error.

        If it is called by the edit_form view, check if title has been updated.
        If so, check if it is unique. If it isn't unique raise an error.
        """
        cleaned_data = self.cleaned_data
        title = cleaned_data['title']
        project = self.instance

        # Check which view is calling the clean function
        if view == 'CreateProject':
            # Check if a project with the same title already exists
            if title and Project.objects.get(title=title):
                raise forms.ValidationError(
                    "This title already exists. Try a different title."
                    )

        elif view == 'EditProject':
            # Only check for existing projects
            # with the same title if the title has changed
            if title and title != project.title and Project.objects.get(
                title=title
            ):
                raise forms.ValidationError(
                    "This title already exists. Try a different title."
                    )

        return cleaned_data


# Create project approvers form to be assigned to a project

class ApproverForm(forms.ModelForm):
    """Create approvers form"""
    class Meta:
        """
        Setup model, fields and widgets for approver form.
        """
        model = ProjectApproval
        fields = ['approver', 'approval_due_by']
        widgets = {
            'approval_due_by': widgets.DateInput(attrs={'type': 'date'})
        }


# Create a formset with Project as parent model and ProjectApproval
# as child model. This is for the create a project view.

ApproverFormSet = inlineformset_factory(
    Project,
    ProjectApproval,
    fields=(
        'approver',
        'approval_due_by'
    ),
    widgets={
            'approval_due_by': widgets.DateInput(attrs={'type': 'date'})
    },
    extra=1,
)

# Create a formset with Project as parent model and ProjectApproval
# as child model. This is for the edit a project view.

EditApproverFormSet = inlineformset_factory(
    Project,
    ProjectApproval,
    fields=(
        'approver',
        'approval_due_by'
    ),
    widgets={
        'approval_due_by': widgets.DateInput(attrs={'type': 'date'})
    },
    extra=0,
    min_num=1
)


class CommentForm(forms.ModelForm):
    """Create comments form to be assigned to a project"""
    class Meta:
        model = Comment
        fields = ('body',)


# Custom signup form

class CustomSignupForm(SignupForm):
    """
    Customise the signup form.

    Add first_name, last_name and department.

    Validate and save the new fields.
    """
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    department = forms.CharField(max_length=80, label='Department')

    def save(self, request):
        """Validate new fields and save"""
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        profile = UserProfile.objects.create(user=user)
        profile.department = self.cleaned_data.get('department')
        profile.save()

        return user
