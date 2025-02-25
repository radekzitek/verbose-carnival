from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OAuthViewSet

router = DefaultRouter()
router.register(r'oauth', OAuthViewSet, basename='oauth')

urlpatterns = [
    path('', include(router.urls)),
]
