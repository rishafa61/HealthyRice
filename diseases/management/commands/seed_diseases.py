from django.core.management.base import BaseCommand

from diseases.models import Disease

DISEASES = [
    dict(
        slug="healthy", name="Healthy", risk_level=Disease.RiskLevel.NONE,
        short_description="Daun padi dalam kondisi sehat, tidak menunjukkan tanda penyakit.",
        symptoms="Warna daun hijau merata\nTidak ada bercak atau lesi\nPertumbuhan normal",
        treatment_steps="Tidak diperlukan penanganan khusus",
        prevention_steps="Lanjutkan praktik budidaya yang baik\nPantau tanaman secara berkala",
    ),
    dict(
        slug="tungro", name="Tungro", risk_level=Disease.RiskLevel.MEDIUM,
        short_description="Daun menguning dari pangkal dan tampak layu pada ujungnya.",
        symptoms="Daun menguning dari pangkal\nPertumbuhan kerdil\nJumlah anakan berkurang",
        treatment_steps="Cabut dan musnahkan tanaman terinfeksi\nKendalikan populasi wereng hijau (vektor)\nGunakan varietas tahan Tungro pada musim tanam berikutnya",
        prevention_steps="Tanam serentak dalam satu hamparan\nGunakan benih bersertifikat\nMonitor populasi wereng hijau secara rutin",
    ),
    dict(
        slug="brown-spot", name="Brown Spot", risk_level=Disease.RiskLevel.MEDIUM,
        short_description="Bercak coklat oval pada permukaan daun, disebabkan jamur Bipolaris oryzae.",
        symptoms="Bercak coklat berbentuk oval dengan pusat abu-abu\nBercak dapat menyatu pada infeksi berat\nDaun mengering dari ujung",
        treatment_steps="Aplikasikan fungisida berbahan aktif mancozeb atau propiconazole\nPerbaiki drainase lahan\nKurangi kepadatan tanam",
        prevention_steps="Gunakan benih bermutu tinggi\nBerikan pemupukan kalium yang cukup\nHindari kekurangan air pada fase generatif",
    ),
    dict(
        slug="blast", name="Blast", risk_level=Disease.RiskLevel.HIGH,
        short_description="Lesi berbentuk belah ketupat dengan pusat abu-abu, disebabkan jamur Magnaporthe oryzae.",
        symptoms="Lesi belah ketupat dengan pusat abu-abu dan tepi coklat\nDapat menyerang daun, leher malai, dan buku batang\nMalai patah pada infeksi leher (neck blast)",
        treatment_steps="Aplikasikan fungisida sistemik segera setelah gejala terlihat\nHindari pemupukan nitrogen berlebihan\nPerbaiki jarak tanam untuk sirkulasi udara",
        prevention_steps="Gunakan varietas tahan blast\nHindari penanaman terlalu rapat\nSeimbangkan dosis pupuk N-P-K",
    ),
    dict(
        slug="blight", name="Blight/Bacterial Blight", risk_level=Disease.RiskLevel.HIGH,
        short_description="Hawar daun bakteri, disebabkan oleh bakteri Xanthomonas oryzae.",
        symptoms="Daun mengering mulai dari tepi berwarna kekuningan hingga putih\nLesi memanjang mengikuti tulang daun\nPada serangan berat, seluruh daun mengering (kresek)",
        treatment_steps="Kurangi pemupukan nitrogen\nPerbaiki sistem drainase, hindari genangan berlebih\nGunakan bakterisida jika serangan berat",
        prevention_steps="Gunakan varietas tahan hawar daun bakteri\nGunakan benih sehat bersertifikat\nHindari melukai tanaman saat perawatan",
    ),
    dict(
        slug="scald", name="Scald", risk_level=Disease.RiskLevel.LOW,
        short_description="Lesi memanjang dengan pola bergelombang seperti terbakar pada ujung daun.",
        symptoms="Lesi berpola bergelombang (seperti bergaris konsentris)\nDimulai dari ujung dan tepi daun\nWarna lesi coklat kekuningan hingga coklat tua",
        treatment_steps="Aplikasikan fungisida jika serangan meluas\nBuang bagian daun yang terinfeksi berat\nJaga keseimbangan hara tanaman",
        prevention_steps="Hindari kelembaban berlebih di sekitar tajuk tanaman\nGunakan jarak tanam yang cukup\nRotasi tanaman bila memungkinkan",
    ),
]


class Command(BaseCommand):
    help = "Seed the 6 disease classes used by the RiceCareAI detection model."

    def handle(self, *args, **options):
        created, updated = 0, 0
        for data in DISEASES:
            obj, was_created = Disease.objects.update_or_create(slug=data["slug"], defaults=data)
            created += was_created
            updated += not was_created
        self.stdout.write(self.style.SUCCESS(f"Seeded diseases: {created} created, {updated} updated."))
