from rest_framework import viewsets
from .models import Event, Topic
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from users.models import Subscription
from .serializers import EventSerializer, TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned events to a given topic,
        by filtering against a `topic` query parameter in the URL.
        """
        queryset = Event.objects.all()
        topic = self.request.query_params.get("topic")
        if topic is not None:
            queryset = queryset.filter(topic__name=topic)
        return queryset


def ping_webhooks(request):
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        # Simulate sending a notification email
        send_mail(
            subject="Webhook Ping Test",
            message="This is a test notification from the /ping endpoint.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
        )
    return JsonResponse(
        {
            "status": "success",
            "message": "Ping notifications sent to all subscribed users.",
        }
    )
