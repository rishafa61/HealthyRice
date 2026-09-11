from django.contrib import admin
from .models import Disease


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "risk_level"]
    prepopulated_fields = {"slug": ("name",)}
