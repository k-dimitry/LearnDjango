# Generated by Django 5.1.7 on 2025-03-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0011_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='woman',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
    ]
