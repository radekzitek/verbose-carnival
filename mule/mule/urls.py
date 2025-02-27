"""
URL Configuration for Mule Project

This module defines the URL patterns for the entire Django project.
It maps URL paths to their corresponding views or includes URL patterns from other apps.

Main URL patterns:
- admin/: Django admin interface for site administration
- oauth2/: OAuth2 provider endpoints for authentication and authorization
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),

    # OAuth2 provider endpoints (login, token, authorize, etc.)
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
