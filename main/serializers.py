from rest_framework import serializers
from .models import Answer, Question


class question_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("user", "title", "body", "created", "answers_count", "points")


class answer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("text", "created", "modified", "points")

