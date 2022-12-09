from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, ProjectApproval, UserProfile, Comment
from django.shortcuts import get_object_or_404
from django.utils import timezone


class TestViews(TestCase):

    @classmethod
    def setUpTestData(self):

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
            id='1',
            owner=get_object_or_404(User, username='testuser')

        )
        self.project.save()

        self.project_approval = ProjectApproval.objects.create(
            project=get_object_or_404(Project, title="This is a project title"),
            approver=get_object_or_404(UserProfile, user=self.user),
            approval_due_by='2023-12-30',
        )

        self.comment = Comment.objects.create(
            project=get_object_or_404(Project, title="This is a project title"),
            name=self.user,
            body='This is a test body comment',
            created_on=timezone.now,
        )

    # test projectList get method returns 200 and dashboard.html
    def test_get_project_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    
    # test MyProjectList get method returns 200 and my-projects.html
    def test_get_MyProjectList(self):
        response = self.client.get('/my-projects')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-projects.html')

    # test MyApprovalList get method returns 200 and my-projects.html
    def test_get_MyApprovalList(self):
        response = self.client.get('/my-approvals')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-approvals.html')


    # test can complete a project
    def test_can_complete_project(self):
        self.client.login(username='testuser', password='CiaoCiao1')
        project = self.project
        response = self.client.post(f'/complete/{project.id}', {'status': 1})
        self.assertRedirects(response, '/my-projects')
        completed_project = Project.objects.get(id=project.id)
        self.assertEqual(completed_project.status, 1)

    # test can approve a project
    def test_can_approve_project(self):
        self.client.login(username='testuser', password='CiaoCiao1')
        project = self.project
        project_approval = self.project_approval
        response = self.client.post(f'/approve/{project.id}', {'approved': True})
        self.assertRedirects(response, '/my-approvals')
        approved_project = ProjectApproval.objects.get(project_id=project.id)
        self.assertEqual(approved_project.approved, True)

    # test can delete a project
    def test_can_delete_project(self):
        project = self.project
        response = self.client.get(f'/delete/{project.id}')
        self.assertRedirects(response, '/my-projects')
        existing_project = Project.objects.filter(id=project.id)
        self.assertEqual(len(existing_project), 0)