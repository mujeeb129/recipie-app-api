from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_user_sucessfull(self):
        user_email = 'test@example.com'
        password = '123@password'
        user = get_user_model().objects.create(
            email=user_email,
            password=password
        )

        self.assertEqual(user.email, user_email)
        self.assertTrue(user.check_password(password))
