# Generated by Django 3.0.8 on 2020-08-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_product_delivery_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='delivery_days',
            field=models.IntegerField(default=1),
        ),
    ]
