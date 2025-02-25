"""
URL configuration for verbose project.
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from apps.metrics.views import MetricsViewSet
from apps.users.views import UserViewSet
from apps.oauth.views import OAuthViewSet

# from . import views

handler404 = "verbose.views.custom_404"

router = DefaultRouter()
router.register(r'metrics', MetricsViewSet, basename='metrics')
router.register(r'users', UserViewSet, basename='users')
router.register(r'oauth', OAuthViewSet, basename='oauth')

urlpatterns = router.urls
