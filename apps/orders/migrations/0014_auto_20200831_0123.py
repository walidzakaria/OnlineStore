# Generated by Django 3.0.8 on 2020-08-30 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200831_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Shipping'),
        ),
    ]
