from rest_framework import serializers
from .models import Answer, Question
from django.utils.html import escape


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("user", "title", "body", "created", "answers_count", "points")


class CreatedField(serializers.RelatedField):
    def to_representation(self, value):
        diff = timezone.now() - value
        return x_ago_helper(diff)


class UserField(serializers.Field):
    def to_representation(self, value):
        return value.username


class AnswerSerializer(serializers.ModelSerializer):
    user = UserField()
    x_ago = serializers.SerializerMethodField()
    text_html = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ("text_html", "x_ago", "user", "id", "points", "hidden")

    def get_text_html(self, obj):
        return urlize(escape(obj.text))

    def get_x_ago(self, obj):
        return x_ago_helper(timezone.now() - obj.created)
