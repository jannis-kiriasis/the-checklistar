from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

# View to render notifications
# From https://www.youtube.com/watch?v=C8pYT1R8yo4&ab_channel=CodeWithStein
# edited as needed


@login_required
def notifications(request):
    """"
    Get goto parameter, notification_id, extra_id.

    If the goto parameter is different from '',
    get the notification with pk=notification_id.

    Evaluate the notification type and redirect to the correct page."
    """
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.COMMENT:
            return redirect('project-details', slug=notification.extra_id)
        elif notification.notification_type == Notification.APPROVAL:
            return redirect('project-details', slug=notification.extra_id)
        elif notification.notification_type == Notification.ADDED_APPROVER:
            return redirect('project-details', slug=notification.extra_id)

    context = {
        'page_title': 'Notifications'
    }
    return render(request, 'notifications.html', context)
