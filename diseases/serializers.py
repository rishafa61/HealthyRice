from rest_framework import serializers
from .models import Disease


class DiseaseSerializer(serializers.ModelSerializer):
    symptoms = serializers.SerializerMethodField()
    treatment_steps = serializers.SerializerMethodField()
    prevention_steps = serializers.SerializerMethodField()

    class Meta:
        model = Disease
        fields = [
            "id", "slug", "name", "short_description",
            "symptoms", "treatment_steps", "prevention_steps",
            "risk_level", "image",
        ]

    def get_symptoms(self, obj):
        return obj.steps_as_list("symptoms")

    def get_treatment_steps(self, obj):
        return obj.steps_as_list("treatment_steps")

    def get_prevention_steps(self, obj):
        return obj.steps_as_list("prevention_steps")


class DiseaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ["id", "slug", "name", "short_description", "risk_level", "image"]
