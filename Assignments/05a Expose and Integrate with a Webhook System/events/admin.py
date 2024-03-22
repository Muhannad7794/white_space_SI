from django.contrib import admin
from .models import Event, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "topic", "venue", "date", "duration"]
    list_filter = ["topic", "date"]
    search_fields = ["name", "venue"]
