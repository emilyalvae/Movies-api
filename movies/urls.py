
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_views = get_schema_view(
    openapi.Info(
        title= "Movie API",
        default_version= "v1",
        description= "API para recordar Dajngo y buscar trabajo",
        terms_of_service= "https://www.google.com/policies/terms/",
        contact= openapi.Contact(email="emilisa23@gmail.com"),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include("movie.urls")),
    path('user/', include("user.urls")),
    path('rent/', include("rent.urls")),
    path('swagger/', schema_views.with_ui("swagger",cache_timeout=0), name="swagger-docs"),
]