# Generated by Django 3.0.8 on 2020-08-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200816_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_ar',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
