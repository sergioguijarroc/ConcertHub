# Generated by Django 4.2.9 on 2024-02-16 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets_app', '0008_alter_reserva_cliente_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente_reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
