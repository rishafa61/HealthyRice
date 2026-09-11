from django.contrib import admin
from .models import Detection


@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    list_display = ["user", "predicted_disease", "confidence", "created_at"]
    list_filter = ["predicted_disease"]
