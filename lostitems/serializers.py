from rest_framework import serializers
from .models import LostItem, Answer, Guess


class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        # fields = "__all__"
        # exclude = ("founder",)
        fields= ["title", "description", "found_at", "category"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = "__all__"
