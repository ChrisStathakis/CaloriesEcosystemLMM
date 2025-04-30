from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from datetime import date
from .models import User, Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="test_name")
        self.profile = Profile.objects.get(user=self.user)
        self.profile.save()

    def test_profile_creation(self):
        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.age, 0)


class UserApiTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('api_register')

    def test_create_user(self):
        user = {
            'username': 'Test12',
            "email": 'test12@gmail.com',
            "password": 'OneLove11',
        }
        response = self.client.post(self.register_url, user, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)