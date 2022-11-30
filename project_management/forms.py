from .models import Project, ProjectApproval, User, UserProfile, Comment
from django import forms

#Create a project form

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'owner', 'description', 'document']


#Create project approvers form to be assigned to a project


class ApproverForm(forms.ModelForm):

    class Meta:
        model = ProjectApproval
        fields = ['approver', 'approver_department', 'approval_due_by']


#Create comments form form to be assigned to a project


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)