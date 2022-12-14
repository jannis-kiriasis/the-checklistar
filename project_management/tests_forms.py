from django.test import TestCase
from .forms import CommentForm, CustomSignupForm, ProjectForm, approver_formset


class TestCommentForm(TestCase):
    """
    Tests fomr comment form.
    """
    def test_comment_body_is_required(self):
        """
        Test that comment body is required.
        If there isn't a body test error is raised.
        """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that comment body is explicit in form metaclass.
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestSignunForm(TestCase):
    """
    Tests for sign up form.
    """
    def test_username_is_required(self):
        """Tests that username is required."""
        form = CustomSignupForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(
            form.errors['username'][0], 'This field is required.'
            )

    def test_first_name_is_required(self):
        """Tests that first_name is required."""
        form = CustomSignupForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.'
            )

    def test_last_name_is_required(self):
        """Tests that last_name is required."""
        form = CustomSignupForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.'
            )

    def test_department_is_required(self):
        """Tests that department is required."""
        form = CustomSignupForm({'department': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('department', form.errors.keys())
        self.assertEqual(
            form.errors['department'][0], 'This field is required.'
            )

    def test_password1_is_required(self):
        """Tests that password1 is required."""
        form = CustomSignupForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(
            form.errors['password1'][0], 'This field is required.'
            )

    def test_password2_is_required(self):
        """Tests that password2 is required."""
        form = CustomSignupForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(
            form.errors['password2'][0], 'This field is required.'
            )
