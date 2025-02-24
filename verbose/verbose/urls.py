"""
URL configuration for verbose project.
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# from . import views

handler404 = "verbose.views.custom_404"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("metrics/", include("apps.metrics.urls")),
    path("users/", include("apps.users.urls")),
    path("oauth/", include("apps.oauth.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
