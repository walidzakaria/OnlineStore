# Generated by Django 3.0.8 on 2020-08-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
