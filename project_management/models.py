from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

PROJECT_STATUS = ((0, 'Not completed'), (1, 'Completed'))


def get_first_last_name(self):
    """
    Change the __str__ of User model.
    """
    return f"{self.first_name} {self.last_name}"


# Call get_first_last_name

User.add_to_class('__str__', get_first_last_name)


class UserProfile(models.Model):
    """
    UserProfile model: stores user information that aren't in User model.
    A user profile belongs only to one user. One user can only have one
    user profile.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='users'
    )
    department = models.CharField(max_length=80)

    def __str__(self):
        """Change display value of User profile"""
        l_name = self.user.last_name
        f_name = self.user.first_name
        dept = self.department
        return f"{f_name} {l_name} | {dept}"


class Project(models.Model):
    """
    Project model. Contains all the information related to a project,
    including the project's approvers
    which are stored in the ProjectApprovers model.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='projects'
    )
    document = CloudinaryField('document', null=True, default=None, blank=True)
    description = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)

    def validate_date(due):
        """
        Due date can't be a past date. If it is, raise error.
        """
        if due < timezone.now().date():
            raise ValidationError('Date cannot be in the past')

    due = models.DateField(validators=[validate_date])

    status = models.IntegerField(choices=PROJECT_STATUS, default=0)

    class Meta:
        ordering = ['-date_created', 'owner']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Create slug from title.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)


class ProjectApproval(models.Model):
    """
    ProjectApprover Model: contains all the information of the approvals.
    One project can have multiple approvals,
    One approval can have only one project.

    NB. Approvals not approvers. This model is for approvers' approvals
    not for approvers. Approvers are users.
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='approvals'
        )
    approver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='approvers'
    )

    approval_date = models.DateField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def validate_date(approval_due_by):
        """
        Due date can't be a past date. If it is, raise error.
        """
        if approval_due_by < timezone.now().date():
            raise ValidationError('Date cannot be in the past')

    approval_due_by = models.DateField(validators=[validate_date])

    approved = models.BooleanField(default=False)

    def __str__(self):
        proj = self.project
        approver = self.approver
        dept = self.approver.department
        return f"Project: {proj} | Approver: {approver} | Department: {dept}"


class Comment(models.Model):
    """
    Comments model. A comment can only have one project. One project
    Can have many comments.
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
