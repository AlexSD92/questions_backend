from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Question
        fields = [
            'id', 'owner', 'question', 'created_at', 'updated_at'
        ]