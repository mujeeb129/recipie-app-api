from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_user_successful(self):
        user_email = 'test@example.com'
        password = '123@password'
        user = get_user_model().objects.create_user(
            email=user_email,
            password=password
        )

        self.assertEqual(user.email, user_email)
        self.assertTrue(user.check_password(password))

    def test_is_email_normalised(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email)
            self.assertEqual(user.email, expected)

    def test_if_email_is_given(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test@123')

    def test_create_superuser(self):

        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test@123'
        )

        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.is_superuser, True)
