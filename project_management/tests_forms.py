from django.test import TestCase
from .forms import CommentForm, CustomSignupForm, ProjectForm, ApproverFormSet


class TestCommentForm(TestCase):

    # test that comment body is required
    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestSignunForm(TestCase):

    # test that username is required
    def test_username_is_required(self):
        form = CustomSignupForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    # test that first_name is required
    def test_first_name_is_required(self):
        form = CustomSignupForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

    # test that last_name is required
    def test_last_name_is_required(self):
        form = CustomSignupForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')


    # test that department is required
    def test_department_is_required(self):
        form = CustomSignupForm({'department': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('department', form.errors.keys())
        self.assertEqual(form.errors['department'][0], 'This field is required.')

    # test that password1 is required
    def test_password1_is_required(self):
        form = CustomSignupForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0], 'This field is required.')

    # test that password2 is required
    def test_password2_is_required(self):
        form = CustomSignupForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'This field is required.')


class TestProjectForm(TestCase):

    # test that title is required
    def test_title_is_required(self):
        form = ProjectForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    # test that owner is required
    def test_owner_is_required(self):
        form = ProjectForm({'owner': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('owner', form.errors.keys())
        self.assertEqual(form.errors['owner'][0], 'This field is required.')

    # test that description is required
    def test_description_is_required(self):
        form = ProjectForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')


    # test that due is required
    def test_due_is_required(self):
        form = ProjectForm({'due': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('due', form.errors.keys())
        self.assertEqual(form.errors['due'][0], 'This field is required.')


# class TestApproverFormSet(TestCase):

#     # test that approver is required
#     def test_approver_is_required(self):
#         form = ApproverFormSet.ProjectApproval({
#             'approver': 'Janins',
#             })
#         self.assertFalse(form.is_valid())
#         self.assertIn('approver', form.errors.keys())
#         self.assertEqual(form.errors['approver'][0], 'This field is required.')