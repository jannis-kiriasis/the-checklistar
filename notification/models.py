from django.db import models
from django.contrib.auth.models import User


# Notification model
# Model from https://www.youtube.com/watch?v=C8pYT1R8yo4&ab_channel=CodeWithStein
# edited as needed

class Notification(models.Model):
    COMMENT = 'comment'
    APPROVAL = 'approval'

    CHOICES = (
        (COMMENT, 'Comment'),
        (APPROVAL, 'Approval')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']


