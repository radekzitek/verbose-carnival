"""
URL Configuration for Mule Project

This module defines the URL patterns for the entire Django project.
It maps URL paths to their corresponding views or includes URL patterns from other apps.

Main URL patterns:
- admin/: Django admin interface for site administration
- oauth2/: OAuth2 provider endpoints for authentication and authorization
"""
from django.contrib import admin
from django.urls import include, path
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(oauth2_urls)),
]
