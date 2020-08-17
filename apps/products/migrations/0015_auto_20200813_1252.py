# Generated by Django 3.0.8 on 2020-08-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_category_name_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='name_ar',
            field=models.CharField(blank=True, max_length=150, verbose_name='Sub-Category-AR'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name_ar',
            field=models.CharField(blank=True, max_length=150, verbose_name='Brand-AR'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ar',
            field=models.CharField(blank=True, max_length=150, verbose_name='Category-AR'),
        ),
    ]