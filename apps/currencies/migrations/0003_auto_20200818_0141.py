# Generated by Django 3.0.8 on 2020-08-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_exchangerate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='exchangerate',
            options={'verbose_name': 'Exchange Rate', 'verbose_name_plural': 'Exchange Rates'},
        ),
        migrations.AlterField(
            model_name='exchangerate',
            name='date',
            field=models.DateTimeField(),
        ),
    ]