# Generated by Django 4.1.7 on 2023-03-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_remove_post_author"),
        ("accounts", "0005_userprofile_pic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="posts",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="posts",
            field=models.ManyToManyField(related_name="posts", to="posts.post"),
        ),
    ]
