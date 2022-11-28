from .models import Project, ProjectApproval, User, UserProfile
from django import forms



# class ProjectForm(forms.ModelForm):

#     title = forms.CharField(
#         required=True,
#     )

#     owners = forms.ModelChoiceField(
#         queryset=User.objects.all()
#     )

#     # document = forms.FileField()

#     description = forms.CharField(
#         required=True,
#         widget=forms.widgets.Textarea(
#             attrs={
#                 "placeholder": "Add your project description...",
#                 "class": "textarea",
#             }
#         ),
#         label="",
#     )

#     approvers = forms.ModelChoiceField(
#         queryset=UserProfile.objects.all()
#     )

#     class Meta:
#         model = Project
#         fields = ['title', 'owner', 'description', 'document', 'approvers']

