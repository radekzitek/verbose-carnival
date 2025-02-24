from django.shortcuts import render  # noqa	F401
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # noqa	F401
import json
from .decorators import require_authentication
from drf_spectacular.utils import extend_schema  # , OpenApiParameter, OpenApiTypes


@extend_schema(
    description="Registers a new user.",
    request=None,  # You can define a serializer for the request body if needed
    responses={
        201: {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string"},
            },
        },
        400: {
            "type": "object",
            "properties": {"error": {"type": "string"}, "details": {"type": "object"}},
        },
        409: {
            "type": "object",
            "properties": {"error": {"type": "string"}, "message": {"type": "string"}},
        },
    },
)
@csrf_exempt
@require_POST
def register_user(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")

        if not username or not password or not email:
            return JsonResponse(
                {
                    "error": "Validation Error",
                    "details": {
                        "username": ["This field is required."] if not username else [],
                        "password": ["This field is required."] if not password else [],
                        "email": ["This field is required."] if not email else [],
                    },
                },
                status=400,
            )

        if (
            User.objects.filter(username=username).exists()
            or User.objects.filter(email=email).exists()
        ):
            return JsonResponse(
                {"error": "Conflict", "message": "Username or email already exists."},
                status=409,
            )

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        return JsonResponse(
            {
                "message": "User registered successfully",
                "username": user.username,
                "email": user.email,
            },
            status=201,
        )

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@extend_schema(
    description="Retrieves the user profile.",
    responses={
        200: {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"type": "string"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
            },
        },
        401: {
            "type": "object",
            "properties": {"error": {"type": "string"}, "message": {"type": "string"}},
        },
    },
)
@require_authentication
@csrf_exempt
@require_GET
def get_user_profile(request):
    user = request.user
    profile_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        # Add other profile fields as needed
    }
    return JsonResponse(profile_data, status=200)


@extend_schema(
    description="Updates the user profile.",
    request=None,  # You can define a serializer for the request body if needed
    responses={
        200: {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "id": {"type": "integer"},
                "username": {"type": "string"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
            },
        },
        400: {"type": "object", "properties": {"error": {"type": "string"}}},
        401: {
            "type": "object",
            "properties": {"error": {"type": "string"}, "message": {"type": "string"}},
        },
    },
)
@require_authentication
@csrf_exempt
@require_http_methods(["PATCH", "PUT"])
def update_user_profile(request):
    try:
        data = json.loads(request.body)
        user = request.user

        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.email = data.get("email", user.email)
        # Update other profile fields as needed

        user.save()
        profile_data = {
            "message": "Profile updated successfully.",
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            # Add other profile fields as needed
        }
        return JsonResponse(profile_data, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
