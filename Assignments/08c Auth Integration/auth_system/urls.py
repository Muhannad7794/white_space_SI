from django.urls import path, include
from django.contrib import admin
# import the swagger schema and urls 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # This includes all the allauth URLs
    #path("api/", include("sso_integration.urls")),
]
