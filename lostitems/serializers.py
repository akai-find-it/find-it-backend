from rest_framework import serializers
from .models import LostItem, Answer, Guess
from categories.serializers import CategorySerializer, QuestionSerializer
from django.contrib.auth import get_user_model


class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "first_name", "last_name"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question_id", "value"]


class AnsweredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question_id", "question"]

    question = QuestionSerializer(read_only=True)


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = "__all__"


class LostItemInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = ["category", "founder", "title", "description", "found_at"]


class LostItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = "__all__"
        read_only_fields = ["founder"]

    category = CategorySerializer(read_only=True)
    founder = FounderSerializer(read_only=True)


class LostItemOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = "__all__"
        read_only_fields = ["founder"]

    category = CategorySerializer()
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    founder = FounderSerializer(read_only=True)
