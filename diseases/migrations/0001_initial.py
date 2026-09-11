from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(blank=True, max_length=255)),
                ('symptoms', models.TextField(blank=True)),
                ('treatment_steps', models.TextField(blank=True)),
                ('prevention_steps', models.TextField(blank=True)),
                ('risk_level', models.CharField(choices=[('none', 'Tidak ada risiko'), ('low', 'Risiko Rendah'), ('medium', 'Risiko Sedang'), ('high', 'Risiko Tinggi')], default='medium', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='diseases/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
