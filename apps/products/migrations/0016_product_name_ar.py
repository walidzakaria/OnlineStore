# Generated by Django 3.0.8 on 2020-08-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200813_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_ar',
            field=models.CharField(blank=True, max_length=255, verbose_name='Product-AR'),
        ),
    ]
