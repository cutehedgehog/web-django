# Generated by Django 4.2.5 on 2023-09-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate_field',
            field=models.IntegerField(default=5),
        ),
    ]
