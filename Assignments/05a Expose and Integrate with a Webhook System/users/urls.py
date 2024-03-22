from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, VerifyEmailView, SubscriptionViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"subscriptions", SubscriptionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "verify-email/<uidb64>/<token>/", VerifyEmailView.as_view(), name="verify_email"
    ),
]
