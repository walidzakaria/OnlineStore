# Generated by Django 3.0.8 on 2020-08-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200820_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, unique=True)),
                ('city_ar', models.CharField(max_length=100, unique=True)),
                ('shipping_fees', models.DecimalField(decimal_places=2, max_digits=17)),
            ],
        ),
    ]