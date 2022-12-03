from .models import Notification

# Create context processor for notifications 
# Code from https://www.youtube.com/watch?v=C8pYT1R8yo4&ab_channel=CodeWithStein


def notifications(request):
    if request.user.is_authenticated:
        return {'notifications': request.user.notifications.filter(is_read=False)}
    else:
        return {'notifications': []}