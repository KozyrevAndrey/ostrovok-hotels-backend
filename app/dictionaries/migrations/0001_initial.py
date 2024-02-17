# Generated by Django 5.0.2 on 2024-02-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                    "name",
                    models.CharField(
                        db_index=True, help_text="City Name", max_length=1000
                    ),
                ),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
            },
        ),
    ]
