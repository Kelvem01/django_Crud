# Generated by Django 4.2.7 on 2023-12-17 20:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inicio", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pessoa",
            old_name="emial",
            new_name="email",
        ),
    ]
