from django.db import models
from django.conf import settings


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, related_name="events", on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)
    date = models.DateTimeField()
    duration = models.DurationField(help_text="Duration in hours and minutes")

    def __str__(self):
        return self.name
