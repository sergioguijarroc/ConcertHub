# Generated by Django 4.2.9 on 2024-02-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0009_concierto_valoracion_media_delete_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concierto',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]