from django.db import models
from django.db.models import Sum, Avg
from cloudinary.models import CloudinaryField

from apps.utils.models import AbstractTableMeta


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Brand')
    name_ar = models.CharField(max_length=150, blank=True, verbose_name='Brand-AR')

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Category')
    name_ar = models.CharField(max_length=150, blank=True, verbose_name='Category-AR')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Sub-Category')
    name_ar = models.CharField(max_length=150, blank=True, verbose_name='Sub-Category-AR')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'Sub-Category'
        verbose_name_plural = 'Sub-Categories'


class Product(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Product')
    name_ar = models.CharField(max_length=255, blank=True, verbose_name='Product-AR')
    keywords = models.CharField(max_length=255, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    price1 = models.DecimalField(max_digits=14, decimal_places=2)
    price2 = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    description = models.TextField(max_length=1000, blank=True, null=True)
    description_ar = models.TextField(max_length=1000, blank=True, null=True)
    ## For demo development
    image1 = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)
    image3 = CloudinaryField('image', blank=True, null=True)
    image4 = CloudinaryField('image', blank=True, null=True)
    image5 = CloudinaryField('image', blank=True, null=True)

    ## For production development
    # image1 = models.ImageField(upload_to='products/', null=True, blank=True)
    # image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    # image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    # image4 = models.ImageField(upload_to='products/', null=True, blank=True)
    # image5 = models.ImageField(upload_to='products/', null=True, blank=True)
    active = models.BooleanField(default=True)
    slider = models.BooleanField(default=False)

    @property
    def purchased(self):
        from apps.orders.models import Purchase
        result = 0
        purchased = Purchase.objects.filter(product=self).aggregate(Sum('quantity'))['quantity__sum']
        if purchased is not None:
            result = purchased
        return result

    @property
    def sold(self):
        from apps.orders.models import OrderItems
        result = 0
        sold = OrderItems.objects.filter(product=self).aggregate(Sum('quantity'))['quantity__sum']
        if sold is not None:
            result = sold
        return result

    @property
    def balance(self):
        return self.purchased - self.sold

    @property
    def number_of_reviews(self):
        return Review.objects.filter(product=self).count()

    @property
    def rating_average(self):
        return Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return f"{self.name} ({self.brand.name})"


class Review(AbstractTableMeta, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    RATING = (
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****"),
    )
    rating = models.SmallIntegerField(choices=RATING, default=1)
    comment = models.TextField(max_length=1000, null=True, blank=True, default='')

    def __str__(self):
        return f'{self.id}: {self.product}, {self.rating}'

    class Meta:
        ordering = ['-id']
