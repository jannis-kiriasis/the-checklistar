from .models import Notification

# function to create a notification
# From https://www.youtube.com/watch?v=C8pYT1R8yo4&ab_channel=CodeWithStein


def create_notification(request, to_user, notification_type, extra_id=0):
    notification = Notification.objects.create(to_user=to_user, notification_type=notification_type, created_by=request.user, extra_id=extra_id)