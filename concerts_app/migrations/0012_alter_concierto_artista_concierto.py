# Generated by Django 4.2.9 on 2024-02-13 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0011_alter_concierto_artista_concierto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concierto',
            name='artista_concierto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts_app.artista'),
        ),
    ]