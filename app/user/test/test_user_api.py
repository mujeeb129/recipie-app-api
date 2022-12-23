"""
Test for the user api
"""
from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


class PublicTests(TestCase):
    """Test the public features of user api"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_successful(self):
        """Test if the user is created successfully"""
        payload = {
            'email': 'test1@example.com',
            'password': 'test@123',
            'confirm_password': 'test@123',
            'name': 'Test User'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload['email'])

        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_already_exists(self):
        """Test if the user with same already exists"""
        payload = {
            'email': 'test1@example.com',
            'password': 'test@123',
            'confirm_password': 'test@123',
            'name': 'Test User'
        }
        create_user(
            email=payload['email'],
            password=payload['password'],
            name=payload['name']
        )

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test if the given password is too short"""
        payload = {
            'email': 'test1@example.com',
            'password': 'test@123',
            'confirm_password': 'test@123',
            'name': 'Test User'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

