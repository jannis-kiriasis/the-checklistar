from .models import Project, ProjectApproval, User, UserProfile
from django import forms


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'owner', 'description', 'document']


class ApproverForm(forms.ModelForm):

    class Meta:
        model = ProjectApproval
        fields = ['approver', 'approver_department', 'approval_due_by']
