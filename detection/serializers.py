from rest_framework import serializers

from diseases.models import Disease
from diseases.serializers import DiseaseListSerializer
from .models import Detection


class DetectionCreateSerializer(serializers.ModelSerializer):
    """Input for POST /api/detections/ — just the image, matching 'Mulai Analisa'."""
    class Meta:
        model = Detection
        fields = ["id", "image"]
        read_only_fields = ["id"]


class DetectionResultSerializer(serializers.ModelSerializer):
    """
    Output shape — matches the 'Prediksi' card in the mockup:
    disease name, risk, confidence %, keterangan singkat, inference time.
    """
    disease = DiseaseListSerializer(source="predicted_disease", read_only=True)

    class Meta:
        model = Detection
        fields = ["id", "image", "disease", "confidence", "inference_time_ms", "created_at"]


class DetectionHistorySerializer(serializers.ModelSerializer):
    """Lighter payload for the Riwayat Deteksi list, with filtering support."""
    disease = DiseaseListSerializer(source="predicted_disease", read_only=True)

    class Meta:
        model = Detection
        fields = ["id", "image", "disease", "confidence", "created_at"]
