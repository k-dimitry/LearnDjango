# Generated by Django 5.1.7 on 2025-03-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_woman_options_woman_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
