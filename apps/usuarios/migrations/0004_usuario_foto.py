# Generated by Django 4.1.7 on 2023-05-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0003_remove_usuario_apellido"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="foto",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
