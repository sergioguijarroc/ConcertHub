# Generated by Django 4.2.9 on 2024-02-16 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
        ('tickets_app', '0005_alter_valoracion_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente_reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.usuario'),
        ),
    ]
