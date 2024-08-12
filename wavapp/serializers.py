from rest_framework import serializers
from .models import WAVFile

class WAVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WAVFile
        fields = ['id', 'file', 'uploaded_at']
