from datetime import date

from django.db import models
from django.db.models import Sum
import pyzt
from django.utils import timezone


from apps.utils.models import AbstractTableMeta
from apps.authapp.models import User
from apps.products.models import Product
from apps.currencies.models import ExchangeRate, Currency


# Create your models here.
class Purchase(AbstractTableMeta, models.Model):
    vendor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    net_price = models.DecimalField(max_digits=14, decimal_places=2)
    product_value = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    __original_product = None

    def __init__(self, *args, **kwargs):
        super(Purchase, self).__init__(*args, **kwargs)
        try:
            self.__original_product = self.product
        except:
            pass

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.product_value = self.quantity * self.net_price
        super(Purchase, self).save(force_insert, force_update, *args, **kwargs)
        if self.__original_product is not None and self.__original_product != self.product:
            self.__original_product.save()
            self.product.save()
        else:
            self.product.save()
        self.__original_product = self.product

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
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    exchange_rate = models.DecimalField(max_digits=17, decimal_places=4, default=0)
    exchanged_due_amount = models.DecimalField(max_digits=17, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.id}: {self.status}'

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        number_of_items = OrderItems.objects.filter(order=self.id).aggregate(Sum('quantity'))['quantity__sum']
        if number_of_items is None:
            self.number_of_items = 0
        else:
            self.number_of_items = number_of_items

        due_amount = OrderItems.objects.filter(
            order=self.id).aggregate(
            Sum('product_value'))['product_value__sum']
        if due_amount is None:
            self.due_amount = 0
        else:
            self.due_amount = due_amount
        exchange_date = self.created_at
        if not exchange_date:
            exchange_date = timezone.now()

        exchange_rate = ExchangeRate.objects.filter(currency=self.currency.id).\
            filter(apply_date__lte=exchange_date).order_by('-apply_date').first()

        if exchange_rate is not None:
            self.exchange_rate = exchange_rate.rate
            self.exchanged_due_amount = self.exchange_rate * self.due_amount
        else:
            self.exchange_rate = 0
            self.exchanged_due_amount = self.due_amount

        super(Order, self).save(force_insert, force_update, *args, **kwargs)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    # To be auto calculated
    product_value = models.DecimalField(max_digits=17, decimal_places=2, default=0)
    __original_product = None
    __original_order = None

    def __init__(self, *args, **kwargs):
        super(OrderItems, self).__init__(*args, **kwargs)
        try:
            self.__original_product = self.product
            self.__original_order = self.order
        except:
            pass

    def __str__(self):
        return f'{self.order}, {self.product}, {self.quantity}, {self.product_value}'

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.product_value = self.quantity * self.product.price1
        super(OrderItems, self).save(force_insert, force_update, *args, **kwargs)
        self.order.save()
        if self.__original_product is not None and self.__original_product != self.product:
            self.__original_product.save()
            self.product.save()
        else:
            self.product.save()
        self.__original_product = self.product

        if self.__original_order is not None and self.__original_product != self.order:
            self.__original_order.save()
            self.order.save()
        else:
            self.order.save()
        self.__original_order = self.order

    class Meta:
        verbose_name = 'Order Items'
        verbose_name_plural = 'Order Items'
