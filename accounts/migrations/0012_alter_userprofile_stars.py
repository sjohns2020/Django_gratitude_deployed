# Generated by Django 4.1.7 on 2023-04-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_userprofile_stars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="stars",
            field=models.IntegerField(default=0),
        ),
    ]
