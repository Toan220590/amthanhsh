from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WAVFileViewSet

router = DefaultRouter()
router.register(r'wav', WAVFileViewSet, basename='wavfile')

urlpatterns = [
    path('', include(router.urls)),
]
