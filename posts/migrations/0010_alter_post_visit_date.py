# Generated by Django 4.1.7 on 2023-03-30 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0009_alter_post_upload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="visit_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]