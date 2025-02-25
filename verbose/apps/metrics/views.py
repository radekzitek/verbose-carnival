from django.shortcuts import render  # noqa	F401
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator


class MetricsViewSet(viewsets.ViewSet):
    @extend_schema(
        description="Endpoint that returns the details of the request.",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "method": {"type": "string", "description": "HTTP method used for the request"},
                    "headers": {"type": "object", "description": "Request headers"},
                    "body": {"type": "string", "description": "Request body"},
                    "path": {"type": "string", "description": "Request path"},
                    "query_params": {"type": "object", "description": "Query parameters"}
                }
            }
        }
    )
    @method_decorator(csrf_exempt)
    def echo(self, request):
        return Response({
            "method": request.method,
            "headers": dict(request.headers),
            "body": request.body.decode('utf-8'),
            "path": request.path,
            "query_params": request.query_params
        })
