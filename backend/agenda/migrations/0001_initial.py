# Generated by Django 3.2.13 on 2022-06-01 19:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RoomModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("name", models.CharField(max_length=144, unique=True)),
            ],
            options={
                "verbose_name": "Room",
                "verbose_name_plural": "Rooms",
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="LectureModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("author", models.CharField(blank=True, max_length=255)),
                ("description", models.CharField(max_length=1000)),
                ("start_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("end_date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lecture_set",
                        to="agenda.roommodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lecture",
                "verbose_name_plural": "Lectures",
                "ordering": ("order",),
            },
        ),
    ]
