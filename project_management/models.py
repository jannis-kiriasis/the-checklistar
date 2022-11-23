from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PROJECT_STATUS = ((0, 'Not completed'), (1, 'Completed'))

# UserProfile model: stores user information that aren't in User model


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='users'
    )
    department = models.CharField(max_length=80)

    def __str__(self):
        return f"Employee: {self.user} | Department: {self.department}"


# Project model. Contains all the information related to a project,
# including the project's approvers
#  which are stored in the ProjectApprovers model


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='projects'
    )
    document = CloudinaryField('image', null=True, default=None, blank=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=PROJECT_STATUS, default=0)
    approvers = models.ManyToManyField(UserProfile)

    class Meta:
        ordering = ['-date_created', 'owner']

    def __str__(self):
        return self.title


# ProjectApprover Model: contains all the information of the approvers.abs
# One project can have multiple approvers,
# One approver can have multiple projects to approve.


class ProjectApproval(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name="approvals"
        )
    approver_department = models.CharField(max_length=80)
    approver = models.ForeignKey(
        UserProfile, on_delete=models.PROTECT, related_name='approvers'
    )
    approval_date = models.DateField(null=True, blank=True)
    approval_due_by = models.DateField(null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Project: {self.project} | Approver: {self.approver} | Department: {self.approver_department}"
