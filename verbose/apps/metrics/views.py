from django.shortcuts import render  # noqa	F401
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from drf_spectacular.utils import extend_schema


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
@csrf_exempt
def echo(request):
    """
    Endpoint that returns the details of the request.
    """
    response_data = {
        "method": request.method,
        "headers": dict(request.headers),
        "body": request.body.decode('utf-8'),
        "path": request.path,
        "query_params": dict(request.GET)
    }
    return HttpResponse(json.dumps(response_data, indent=4), content_type="application/json")
