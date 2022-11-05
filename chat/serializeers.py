from rest_framework import serializers
from .models import NotificationToken

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationToken
        fields = ["token", "user"]