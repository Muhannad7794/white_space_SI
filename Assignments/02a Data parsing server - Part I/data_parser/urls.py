from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("parser/", include("parser.urls")),
    # DRF's browsable API
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Schema and Documentation paths for drf-spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional: Use SpectacularSwaggerView for Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
