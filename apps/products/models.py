from django.db import models
from apps.utils.models import AbstractTableMeta


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Brand')

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Category')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Sub-Category')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'Sub-Category'
        verbose_name_plural = 'Sub-Categories'


class Product(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Product')
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    price1 = models.DecimalField(max_digits=14, decimal_places=2)
    price2 = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    description = models.TextField(max_length=500, blank=True, null=True)
    image1 = models.ImageField(upload_to='products/', null=True)
    image2 = models.ImageField(upload_to='products/', null=True)
    image3 = models.ImageField(upload_to='products/', null=True)
    image4 = models.ImageField(upload_to='products/', null=True)
    image5 = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return f"{self.name} ({self.brand.name})"
