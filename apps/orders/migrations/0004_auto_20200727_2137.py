# Generated by Django 3.0.8 on 2020-07-27 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_purchase_net_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name': 'Order Items', 'verbose_name_plural': 'Order Items'},
        ),
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name': 'User Address', 'verbose_name_plural': 'User Addresses'},
        ),
    ]
