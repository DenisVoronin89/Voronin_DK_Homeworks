# Generated by Django 4.1.7 on 2023-07-03 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
