# Generated by Django 3.0.8 on 2020-08-16 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_recommended'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='recommended',
            new_name='slider',
        ),
    ]
