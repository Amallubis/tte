# Generated by Django 4.2.5 on 2023-09-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Berita",
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
                ("fotos", models.ImageField(upload_to="foto/")),
                ("judul", models.CharField(max_length=200)),
                ("postingan", models.TextField()),
                ("publish", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]