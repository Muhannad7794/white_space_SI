from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Event, Topic
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from users.models import Subscription
from .serializers import EventSerializer, TopicSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    tags=["Topics"],
    summary="The opics act as the a ctagorization key for the events. \
        the user can filter the evnet accrording to the topics, \
        and the subscription system will notify the user when any \
        changes are applied to any of the topics they are subscribed to.",
    description="CRUD operations for topics.",
)
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


@extend_schema_view(
    tags=["Events"],
    summary="the events act as sub instances of the topics. \
        when a new event is created in a certain topic, \
        the subscription system will notify the users subscribed to that topic.\
        This makes the events app the exposee , and the users app the integrator.",
    description="CRUD operations for events.",
)
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


@extend_schema(
    tags=["Webhooks"],
    summary="triggers the ping endpoint to send notifications to all subscribed users.\
            Used as a test endpoint to verify the webhook system is working.",
    description="Sends a test notification to all subscribed users via email.",
    responses={200: "Ping notifications sent to all subscribed users."},
)
class PingWebhooksView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request, *args, **kwargs):
        subscriptions = Subscription.objects.all()
        for subscription in subscriptions:
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
