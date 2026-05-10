from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(ReadOnlyModelViewSet):
    queryset = Doctor.objects.filter(is_active=True)
    serializer_class = DoctorSerializer
