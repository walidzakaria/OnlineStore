# Generated by Django 3.0.8 on 2020-08-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_slider_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='lang',
            field=models.CharField(choices=[('en', 'EN'), ('ar', 'AR'), ('both', 'Both')], default='both', max_length=4),
        ),
    ]
