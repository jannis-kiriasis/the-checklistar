from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PROJECT_STATUS = ((0, 'Not completed'), (1, 'Completed'))
APPROVAL_STATUS = ((0, 'Not approved'), (1, 'Approved'))


# ProjectApprover Model: contains all the information of the approvers.abs
# One project can have multiple approvers,
# One approver can have multiple projects to approve.


class ProjectApprover(models.Model):
    approver_department = models.CharField(max_length=80)
    approver = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='approvers'
    )
    approval_date = models.DateField(null=True, blank=True)
    approval_due_by = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=APPROVAL_STATUS, default=0)

    def __str__(self):
        return f"Project: {self.project} | Approver: {self.approver} | Department: {self.approver_department}"


# Project model. Contains all the information related to a project,
# including the project's approvers
#  which are stored in the ProjectApprovers model


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='projects'
    )
    document = CloudinaryField('')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approvers = models.ManyToManyField(ProjectApprover, related_name='project')
    status = models.IntegerField(choices=PROJECT_STATUS, default=0)

    class Meta:
        ordering = ['-date_created', 'owner']

    def __str__(self):
        return self.title


# UserProfile model: stores user information that aren't in User model


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users'
    )
    department = models.CharField(max_length=80)

    def __str__(self):
        return f"Employee: {self.user} | Department: {self.department}"
