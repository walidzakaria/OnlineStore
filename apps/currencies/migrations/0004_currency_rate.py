# Generated by Django 3.0.8 on 2020-08-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_auto_20200818_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=14),
        ),
    ]
