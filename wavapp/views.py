from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import WAVFile
from .serializers import WAVFileSerializer



class WAVFileViewSet(viewsets.ModelViewSet):
    queryset = WAVFile.objects.all()
    serializer_class = WAVFileSerializer
    parser_classes = [MultiPartParser, FormParser]
