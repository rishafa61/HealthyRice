from django.conf import settings
from django.db import models

from diseases.models import Disease


def detection_image_path(instance, filename):
    return f"detections/user_{instance.user_id}/{filename}"


class Detection(models.Model):
    """
    One row per scan. This is what backs the 'Riwayat Deteksi' (history)
    screen and is what "Send photo to Disease Detector API" ultimately
    produces and saves.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="detections")
    image = models.ImageField(upload_to=detection_image_path)
    predicted_disease = models.ForeignKey(
        Disease, on_delete=models.PROTECT, related_name="detections", null=True, blank=True
    )
    confidence = models.FloatField(default=0)  # 0-100
    inference_time_ms = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} -> {self.predicted_disease} ({self.confidence:.1f}%)"
