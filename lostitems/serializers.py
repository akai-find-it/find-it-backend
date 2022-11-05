from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import LostItem, Answer, Guess
from categories.serializers import CategorySerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = "__all__"

class LostItemInputSerializer(serializers.Serializer):
    class Meta:
        model = LostItem
        fields = ["category", "title", "description", "found_at", "founder", "answers"]
        read_only_fields = ["founder"]

        def create(self, validated_data):
                answers = validated_data.pop('answer')
                item = LostItem.objects.create(**validated_data)
                for answer in answers:
                    Answer.objects.create(item=item, **answer)
                return item

class LostItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = "__all__"
        read_only_fields = ["founder"]

    category = CategorySerializer(read_only=True)


class LostItemOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = "__all__"
        read_only_fields = ["founder"]

    category = CategorySerializer()
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    founder = serializers.SlugRelatedField(many=True, read_only=True, slug_field="first_name")
