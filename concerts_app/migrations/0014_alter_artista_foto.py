# Generated by Django 4.2.9 on 2024-02-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts_app', '0013_alter_concierto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto',
            field=models.ImageField(upload_to='artistas'),
        ),
    ]
