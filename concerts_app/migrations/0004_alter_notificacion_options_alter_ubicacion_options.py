# Generated by Django 4.2.9 on 2024-01-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0003_review_cliente_review_review_concierto_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notificacion',
            options={'verbose_name_plural': 'Notificaciones'},
        ),
        migrations.AlterModelOptions(
            name='ubicacion',
            options={'verbose_name_plural': 'Ubicaciones'},
        ),
    ]
