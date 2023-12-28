# Generated by Django 4.2.7 on 2023-12-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inicio", "0003_alter_pessoa_options_alter_pessoa_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                ("descricao", models.TextField(blank=True, verbose_name="Descrição")),
            ],
        ),
    ]
