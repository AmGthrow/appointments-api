# Generated by Django 5.0.6 on 2024-06-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0001_initial"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="patients",
        ),
        migrations.AddField(
            model_name="appointment",
            name="patients",
            field=models.ManyToManyField(to="patients.patient"),
        ),
    ]