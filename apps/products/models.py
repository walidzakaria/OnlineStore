from django.db import models
from apps.utils.models import AbstractTableMeta


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return f"<Brand {self.id}, Name: {self.name}>"


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return f"<Category {self.id}, Name: {self.name}>"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"<SubCategory {self.id}, Name: {self.name}, Category: {self.category.name}>"

    class Meta:
        verbose_name = 'Sub-Category'
        verbose_name_plural = 'Sub-Categories'


class Product(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=255, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    price1 = models.DecimalField(max_digits=14, decimal_places=2)
    price2 = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"<Product {self.id}, Name: {self.name}, Brand: {self.brand}, Price1: {self.price1}, Price2: {self.price2}>"
