# Generated by Django 4.2 on 2023-04-25 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_sellerdetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="SellerRating",
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
                ("rating", models.IntegerField()),
                ("review", models.TextField(blank=True, null=True)),
                ("dateCreated", models.DateTimeField(auto_now_add=True)),
                (
                    "sellerId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller_rates",
                        to="users.seller",
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_rating",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Seller Ratings",
                "verbose_name_plural": "Seller Ratings",
            },
        ),
    ]
