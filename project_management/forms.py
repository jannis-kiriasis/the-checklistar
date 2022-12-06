from .models import Project, ProjectApproval, User, UserProfile, Comment
from django import forms
from django.forms import inlineformset_factory, widgets
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create a project form


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'owner', 'description', 'document', 'due']
        widgets = {
            'due': widgets.DateInput(attrs={'type': 'date'})
        }

    def clean_due(self, *args, **kwargs):
        due = self.cleaned_data.get("due")
        if due:
            if due < timezone.now().date():
                raise ValidationError(
                    "Please enter a valid due date! It can't be in the past."
                )
        return due


# Create project approvers form to be assigned to a project

class ApproverForm(forms.ModelForm):

    class Meta:
        model = ProjectApproval
        fields = ['approver', 'approval_due_by']
        widgets = {
            'approval_due_by': widgets.DateInput(attrs={'type': 'date'})
        }


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

# Create comments form form to be assigned to a project


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


