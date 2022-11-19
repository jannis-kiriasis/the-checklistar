from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PROJECT_STATUS = ((0, "Not completed"), (1, "Completed"))
APPROVAL_STATUS = ((0, "Not approved"), (1, "Approved"))

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="projects"
    )
    document = CloudinaryField('')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=PROJECT_STATUS, default=0)

    class Meta:
        ordering = ['-date_created', 'owner']

    def __str__(self):
        return self.title
