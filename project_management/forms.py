from .models import Project, ProjectApproval, User, UserProfile, Comment
from django import forms
from django.forms import inlineformset_factory, widgets
from django.utils import timezone
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm


# Create a project form


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'owner', 'description', 'document', 'due']
        widgets = {
            'due': widgets.DateInput(attrs={'type': 'date'})
        }


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


# Custom signup form

class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    department = forms.CharField(max_length=80, label='Department')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        profile = UserProfile.objects.create(user=user)
        profile.department = self.cleaned_data.get('department')
        profile.save()

        return user