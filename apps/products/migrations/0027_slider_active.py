# Generated by Django 3.0.8 on 2020-08-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_remove_product_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]