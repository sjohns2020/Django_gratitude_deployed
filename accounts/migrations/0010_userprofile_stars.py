# Generated by Django 4.1.7 on 2023-04-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_remove_userprofile_posts"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="stars",
            field=models.IntegerField(default=0),
        ),
    ]
