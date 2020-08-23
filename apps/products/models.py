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
    reduction = models.DecimalField(max_digits=14, decimal_places=2, default=0)
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
    purchased = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    balance = models.IntegerField(default=0)
    rating_average = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, default=5.00)
    number_of_reviews = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.calculate()
        self.calc_reviews()
        super(Product, self).save(*args, **kwargs)

    def calculate(self):
        from apps.orders.models import Purchase, OrderItems
        purchased = Purchase.objects.filter(product=self).aggregate(Sum('quantity'))['quantity__sum']
        if purchased is None:
            purchased = 0
        sold = OrderItems.objects.filter(product=self).aggregate(Sum('quantity'))['quantity__sum']
        if sold is None:
            sold = 0
        balance = purchased - sold

        # apply changes
        if self.price2 == 0:
            self.reduction = 0
        else:
            self.reduction = (self.price2 - self.price1) / self.price2
        self.purchased = purchased
        self.sold = sold
        self.balance = balance

    def calc_reviews(self):
        number_of_reviews = Review.objects.filter(product=self).count()
        rating_average = Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']

        # apply changes
        self.number_of_reviews = number_of_reviews
        self.rating_average = rating_average

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
    rating = models.SmallIntegerField(choices=RATING, default=5)
    comment = models.TextField(max_length=1000, null=True, blank=True, default='')
    __original_product = None

    def __init__(self, *args, **kwargs):
        super(Review, self).__init__(*args, *kwargs)
        try:
            self.__original_product = self.product
        except:
            pass

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        super(Review, self).save(force_insert, force_update, *args, **kwargs)
        if self.__original_product is not None and self.__original_product != self.product:
            self.__original_product.save()
            self.product.save()
        else:
            self.product.save()
        self.__original_product = self.product

    def __str__(self):
        return f'{self.id}: {self.product}, {self.rating}'

    class Meta:
        ordering = ['-id']


class Slider(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Slider')
    ## For demo development
    image = CloudinaryField('image', blank=True, null=True)

    ## For production development
    # image = models.ImageField(upload_to='products/', null=True, blank=True)
    link = models.CharField(max_length=255)
    LANG = (
        ('en', 'EN'),
        ('ar', 'AR'),
        ('both', 'Both'),
    )
    lang = models.CharField(max_length=4, choices=LANG, default='both')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.link})"
