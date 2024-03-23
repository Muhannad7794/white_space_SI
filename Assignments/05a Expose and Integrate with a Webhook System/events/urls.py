from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TopicViewSet, ping_webhooks

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"topics", TopicViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("ping/", ping_webhooks),
]
