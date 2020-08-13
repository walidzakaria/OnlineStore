from django.db import models
from django.db.models import Sum

from apps.utils.models import AbstractTableMeta
from apps.authapp.models import User
from apps.products.models import Product


# Create your models here.
class Purchase(AbstractTableMeta, models.Model):
    vendor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    net_price = models.DecimalField(max_digits=14, decimal_places=2)

    @property
    def product_value(self):
        return self.quantity * self.net_price

    def __str__(self):
        return f'{self.id}: {self.product}: {self.quantity}, {self.product_value}'

    class Meta:
        ordering: ['-id']


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.user}: {self.address}'

    class Meta:
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'


class Order(AbstractTableMeta, models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    STATUS = (
        ('Preparation', 'Preparation'),
        ('Delivery', 'Delivery'),
        ('Delivered', 'Delivered'),
        ('Delivery Back', 'Delivery Back'),
        ('Cancelled', 'Cancelled'),
    )

    status = models.CharField(max_length=15, choices=STATUS, default='Preparation')
    user_address = models.ForeignKey(UserAddress, on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True, default='')
    # To be auto calculated
    number_of_items = models.PositiveIntegerField(default=0)
    due_amount = models.DecimalField(max_digits=17, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.id}: {self.status}'

    def calculate(self):
        self.number_of_items = OrderItems.objects.filter(order=self.id).aggregate(Sum('quantity'))['quantity__sum']
        self.due_amount = OrderItems.objects.filter(
            order=self.id).aggregate(
            Sum('product_value'))['product_value__sum']
        self.save()


# Just test
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    # To be auto calculated
    product_value = models.DecimalField(max_digits=17, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.order}, {self.product}, {self.quantity}, {self.product_value}'

    def calculate(self):
        self.product_value = self.quantity * self.product.price1
        self.save()

    class Meta:
        verbose_name = 'Order Items'
        verbose_name_plural = 'Order Items'
