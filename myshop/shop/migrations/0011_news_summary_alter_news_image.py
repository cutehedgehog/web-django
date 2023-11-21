# Generated by Django 4.2.5 on 2023-09-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_provider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='summary',
            field=models.TextField(default='news text'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='media/Sheba_Logo.png', upload_to='user/'),
        ),
    ]