# Generated by Django 4.1.5 on 2023-02-10 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="user/images/profile/%Y/%m/%d"
                    ),
                ),
                ("phone_num", models.IntegerField(blank=True, null=True, unique=True)),
                ("height", models.FloatField(blank=True, null=True)),
                ("weight", models.FloatField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
