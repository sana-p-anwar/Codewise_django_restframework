from rest_framework import serializers
from repository.models import QuestionDB


class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 200)
    language = serializers.ChoiceField(choices = QuestionDB.LANGUAGE_CHOICES,default = "python")
    difficulty_level = serializers.ChoiceField(choices =  QuestionDB.DIFFICULTY_CHOICES,default = "python")
    topic = serializers.CharField(max_length = 200)
    notes = serializers.CharField(max_length = 1000)
    published_date = serializers.DateTimeField(read_only=True)
    sample_input = serializers.CharField(max_length = 1000)
    sample_output = serializers.CharField(max_length = 1000)
    is_active = serializers.BooleanField(default=True)
