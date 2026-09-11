from rest_framework import viewsets, permissions
from .models import Disease
from .serializers import DiseaseSerializer, DiseaseListSerializer


class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Disease.objects.all()
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return DiseaseListSerializer
        return DiseaseSerializer
