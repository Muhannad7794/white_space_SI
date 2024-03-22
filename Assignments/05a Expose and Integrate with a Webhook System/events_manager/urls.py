from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "users/", include("users.urls")
    ),  # Include the users app URLs under the 'api/' namespace
    # Schema and Documentation paths
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # API schema
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # Swagger UI
]
