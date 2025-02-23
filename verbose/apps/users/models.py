from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    reset_token = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.user.username
