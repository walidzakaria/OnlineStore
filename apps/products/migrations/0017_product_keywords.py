# Generated by Django 3.0.8 on 2020-08-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_name_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]