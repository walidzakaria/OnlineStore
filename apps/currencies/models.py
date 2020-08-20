from django.db import models

from apps.utils.models import AbstractTableMeta


# Create your models here.
class Currency(models.Model):
    currency = models.CharField(max_length=20, unique=True)
    currency_ar = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=3, unique=True)
    rate = models.DecimalField(max_digits=14, decimal_places=4,default=0)

    def __str__(self):
        return f'{self.currency}, {self.code}'

    def calculate(self):
        last_rate = ExchangeRate.objects.filter(currency=self.id)\
            .order_by('-apply_date').first()
        self.rate = last_rate.rate
        self.save()

    class Meta:
        ordering = ['id']
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class ExchangeRate(AbstractTableMeta, models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    apply_date = models.DateTimeField()
    rate = models.DecimalField(max_digits=14, decimal_places=4)

    def __str__(self):
        return f'{self.currency.code}, {self.rate}'

    class Meta:
        ordering: ['-apply_date']
        verbose_name = 'Exchange Rate'
        verbose_name_plural = 'Exchange Rates'


