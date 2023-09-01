from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework import permissions 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 


schema_view = get_schema_view(
    openapi.Info(
        title="Nichangie API",
        default_version="v1",
        description="An API for the Nichangie App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="welcome@nichangie.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('api/v1/', include('campaign.urls')),
    path('api/v1/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    
    # path('openapi', get_schema_view(
    #         title="Nichangie API",
    #         description="An API for the Nichangie App",
    #         version="1.0.0"
    #     ), name='openapi-schema'),
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
