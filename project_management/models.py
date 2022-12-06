from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

PROJECT_STATUS = ((0, 'Not completed'), (1, 'Completed'))

# UserProfile model: stores user information that aren't in User model


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='users'
    )
    department = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.user} | {self.department}"


# Project model. Contains all the information related to a project,
# including the project's approvers
#  which are stored in the ProjectApprovers model


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='projects'
    )
    document = CloudinaryField('document', null=True, default=None, blank=True)
    description = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)

    def validate_date(due):
        if due < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

    due = models.DateField(validators=[validate_date])

    status = models.IntegerField(choices=PROJECT_STATUS, default=0)

    class Meta:
        ordering = ['-date_created', 'owner']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)


# ProjectApprover Model: contains all the information of the approvers.abs
# One project can have multiple approvers,
# One approver can have multiple projects to approve.


class ProjectApproval(models.Model):

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="approvals"
        )
    approver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='approvers'
    )

    approval_date = models.DateField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def validate_date(approval_due_by):
        if approval_due_by < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

    approval_due_by = models.DateField(validators=[validate_date])

    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Project: {self.project} | Approver: {self.approver} | Department: {self.approver.department}"
    



# Comments model


class Comment(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name="comments"
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"