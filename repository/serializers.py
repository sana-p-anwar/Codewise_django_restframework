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

class SubmissionSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer=serializers.CharField()
    points =serializers.IntegerField(read_only=True)
    owner=serializers.CharField()
    remarks=serializers.CharField(required=False, allow_blank=True)
    submission_date=serializers.DateTimeField(read_only=True)

    def validate(self, validate_data):
        question_id = validate_data.get("question_id")
        if not QuestionDB.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exist...!")
        return validate_data