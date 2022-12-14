from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'code', 'language']