from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TopicViewSet, PingWebhooksView

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")
router.register(r"topics", TopicViewSet, basename="topic")

urlpatterns = [
    path("", include(router.urls)),
    path("ping/", PingWebhooksView.as_view(), name="ping_webhooks"),
]
