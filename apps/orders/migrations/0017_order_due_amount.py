# Generated by Django 3.0.8 on 2020-08-31 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20200831_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=17),
        ),
    ]
