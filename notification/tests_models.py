from django.test import TestCase
from .models import Notification
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone


# Test notification model.
class TestModels(TestCase):

    @classmethod
    def setUpTestData(self):

        self.user = User.objects.create(username='testuser')
        self.user.set_password('CiaoCiao1')
        self.user.save()

        self.notification = Notification.objects.create(
            to_user=self.user,
            notification_type='comment',
            created_by=self.user
        )
        self.notification.save()

    # project test is_read has default value
    def test_default_notification_values(self):
        self.assertFalse(self.notification.is_read)
