# Generated by Django 4.2 on 2023-05-01 06:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="shop",
        ),
    ]