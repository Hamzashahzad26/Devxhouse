# Generated by Django 4.2.2 on 2023-07-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(upload_to='featured_image_%Y_%m_%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='featured_image_%Y_%m_%d'),
        ),
    ]