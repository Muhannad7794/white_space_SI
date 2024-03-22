from rest_framework import viewsets
from .models import Event, Topic
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
