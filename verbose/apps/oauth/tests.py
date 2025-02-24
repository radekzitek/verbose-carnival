from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json


class OAuth2Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            "username": "testuser",
            "password": "testpassword123",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_register_user(self):
        response = self.client.post(
            reverse("register_user"),
            data=json.dumps(self.user_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())
        self.assertIn("username", response.json())
        self.assertIn("email", response.json())

    def test_oauth_token(self):
        response = self.client.post(
            reverse("oauth_token"),
            data=json.dumps(
                {
                    "username": self.user_data["username"],
                    "password": self.user_data["password"],
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())
        self.assertIn("refresh_token", response.json())

    def test_logout(self):
        response = self.client.post(reverse("logout"), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_refresh_token(self):
        oauth_token_response = self.client.post(
            reverse("oauth_token"),
            data=json.dumps(
                {
                    "username": self.user_data["username"],
                    "password": self.user_data["password"],
                }
            ),
            content_type="application/json",
        )
        refresh_token = oauth_token_response.json().get("refresh_token")

        response = self.client.post(
            reverse("refresh_token"),
            data=json.dumps({"refresh_token": refresh_token}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())
