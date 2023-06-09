# Generated by Django 4.1.7 on 2023-03-27 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Org",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("website", models.CharField(max_length=255)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("stars", models.IntegerField()),
                (
                    "upload",
                    models.ImageField(
                        default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLrWVtomuKNMXY38fiZ6HM7PJSiE7ubfdfvQbdAXC9&s",
                        upload_to="uploads/%Y/%m/%d/",
                    ),
                ),
            ],
        ),
    ]
