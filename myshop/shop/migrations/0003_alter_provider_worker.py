# Generated by Django 4.2.5 on 2023-09-22 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_productcategory_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='providers', to=settings.AUTH_USER_MODEL),
        ),
    ]
