from rest_framework import serializers

from .event_handlers.event_mapper import EventMapper



class WebhookPayloadSerializer(serializers.Serializer):
    event = serializers.CharField()
    merchant = serializers.CharField()
    created_at = serializers.CharField()
    data = serializers.JSONField() 