# Generated by Django 5.0.4 on 2024-04-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_pic",
            field=models.URLField(
                default="https://res.cloudinary.com/dybwn1q6h/image/upload/v1712654306/profile_default_arc6ar.jpg"
            ),
        ),
    ]
