# Generated by Django 4.2.2 on 2023-07-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
