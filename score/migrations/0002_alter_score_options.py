# Generated by Django 5.0 on 2024-02-06 20:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("score", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="score",
            options={"ordering": ["-value"]},
        ),
    ]
