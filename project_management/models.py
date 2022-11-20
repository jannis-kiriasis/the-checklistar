from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PROJECT_STATUS = ((0, 'Not completed'), (1, 'Completed'))
APPROVAL_STATUS = ((0, 'Not approved'), (1, 'Approved'))

# Create your models here.

# Project model. Contains all the information related to a project


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='projects'
    )
    document = CloudinaryField('')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=PROJECT_STATUS, default=0)

    class Meta:
        ordering = ['-date_created', 'owner']

    def __str__(self):
        return self.title


# ProjectApprover Model: contains all the information to the project's approvers
class ProjectApprover(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name='approvers'
        )
    approver_department = models.CharField(max_length=80)
    approver = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='approvers'
    )
    approval_date = models.DateField(null=True, blank=True)
    approval_due_by = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=APPROVAL_STATUS, default=0)

    class Meta:
        ordering = ['approval_date', 'project']

    def __str__(self):
        return f"Project: {self.project} | Approver: {self.approver} | Department: {self.approver_department}"

# UserProfile model: stores user information that aren't in User model


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users'
    )
    department = models.CharField(max_length=80)

    def __str__(self):
        return f"Employee: {self.user} | Department: {self.department}"
