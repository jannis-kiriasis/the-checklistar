from django.test import TestCase
from .models import Project, ProjectApproval, UserProfile, User, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone


class TestModels(TestCase):

    @classmethod
    def setUpTestData(self):
        """Setup records for tests."""
        self.user = User.objects.create(username='testuser')
        self.user.set_password('CiaoCiao1')
        self.user.save()
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.user_profile.department = "marketing"
        self.user_profile.save()

        self.project = Project.objects.create(
            title='This is a project title',
            slug='this-is-a-project-title',
            description='This is a text description',
            due='2021-12-30',
            owner=get_object_or_404(User, username='testuser')
        )
        self.project.save()

        self.project_approval = ProjectApproval.objects.create(
            project=get_object_or_404(
                Project, title="This is a project title"
                ),
            approver=get_object_or_404(UserProfile, user=self.user),
            approval_due_by='2023-12-30',
        )

        self.comment = Comment.objects.create(
            project=get_object_or_404(
                Project, title="This is a project title"
                ),
            name=self.user,
            body='This is a test body comment',
            created_on=timezone.now,
        )

    def test_project_str(self):
        """Tests that project __str__ is equal to the project title."""
        self.assertEqual(str(self.project), 'This is a project title')

    def test_default_project_values(self):
        """Tests that project default values are actually defaulted."""
        self.assertEqual(self.project.status, 0)
        self.assertEqual(self.project.document, None)

    def test_project_approval_default_values(self):
        """
        Tests that project approval default values are actually defaulted.
        """
        self.assertFalse(self.project_approval.approved)

    def test_project_approval_approver_FK(self):
        """project_approval.approver is connected to an existing UserProfile"""
        self.assertEqual(self.project_approval.approver, self.user_profile)

    def test_project_approval_project_FK(self):
        """
        Test project_approval.project is connected to an existing Project
        """
        self.assertEqual(self.project_approval.project, self.project)

    def test_project_commnet_project_is_FK(self):
        """test comment is connected to an existing Project"""
        self.assertEqual(self.comment.project, self.project)
