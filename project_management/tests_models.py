from django.test import TestCase
from .models import Project, ProjectApproval, UserProfile, User
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestModels(TestCase):

    @classmethod
    def createTestData(self):

        self.user = User.objects.create(username='testuser')
        self.user.set_password('CiaoCiao1')
        self.user.save()

        self.project = Project.objects.create(
                title='This is a project title',
                slug='this-is-a-project-title',
                description='This is a text description',
                due='2021-12-30',
                owner=get_object_or_404(User, username='testuser')

        )

    # project __str__ is equal to the project title   
    def test_project_str(self):
        self.assertEqual(str(self.project), 'This is a project title')

    # project test default values are actually defaulted   
    def test_default_project_values(self):
        self.assertEqual(self.project.status, 0)
        self.assertEqual(self.project.document, None)

    