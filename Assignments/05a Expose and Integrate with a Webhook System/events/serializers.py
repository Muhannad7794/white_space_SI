from rest_framework import serializers
from .models import Event, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source="topic.name", read_only=True)

    class Meta:
        model = Event
        fields = ["id", "name", "topic", "topic_name", "venue", "date", "duration"]
        extra_kwargs = {"topic": {"write_only": True}}
