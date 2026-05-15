# urls.py

from django.urls import path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import (
    AgentCreateAPIView,
    LeadCreateAPIView,
    AgentListAPIView,
    LeadListAPIView
)


schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="CRM Lead Assignment APIs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    # Swagger URLs

    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),

    path(
        'redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='schema-redoc'
    ),

    path(
        'swagger.json',
        schema_view.without_ui(
            cache_timeout=0
        ),
        name='schema-json'
    ),


    # API URLs

    path(
        "create-agent/",
        AgentCreateAPIView.as_view()
    ),

    path(
        "create-lead/",
        LeadCreateAPIView.as_view()
    ),

    path(
        "agents/",
        AgentListAPIView.as_view()
    ),

    path(
        "leads/",
        LeadListAPIView.as_view()
    ),

]