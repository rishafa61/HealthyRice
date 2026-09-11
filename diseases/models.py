from django.db import models


class Disease(models.Model):
    class RiskLevel(models.TextChoices):
        NONE = "none", "Tidak ada risiko"
        LOW = "low", "Risiko Rendah"
        MEDIUM = "medium", "Risiko Sedang"
        HIGH = "high", "Risiko Tinggi"

    slug = models.SlugField(unique=True)  # e.g. "tungro", "brown-spot" — this is the ML class label
    name = models.CharField(max_length=100)  # display name, e.g. "Tungro"
    short_description = models.CharField(max_length=255, blank=True)  # "Keterangan Singkat" on prediction card
    symptoms = models.TextField(blank=True)  # "Gejala"
    treatment_steps = models.TextField(blank=True)  # "Langkah Penanganan" — one step per line
    prevention_steps = models.TextField(blank=True)  # "Pencegahan" — one step per line
    risk_level = models.CharField(max_length=10, choices=RiskLevel.choices, default=RiskLevel.MEDIUM)
    image = models.ImageField(upload_to="diseases/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def steps_as_list(self, field_name):
        raw = getattr(self, field_name) or ""
        return [line.strip() for line in raw.splitlines() if line.strip()]
