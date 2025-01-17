# Generated by Django 4.2.9 on 2024-01-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0005_artista_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='concierto',
            name='descripcion',
            field=models.TextField(default='No description available'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concierto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='conciertos'),
        ),
    ]
