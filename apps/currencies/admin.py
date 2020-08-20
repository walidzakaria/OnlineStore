from django.contrib import admin

from .models import Currency, ExchangeRate
from .forms import ExchangeRateForm


# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'currency_ar', 'code', 'rate',)
    search_fields = ('currency', 'currency_ar', 'code',)
    readonly_fields = ('rate', )


class ExchangeRateAdmin(admin.ModelAdmin):
    form = ExchangeRateForm
    list_display = ('id', 'get_currency', 'apply_date', 'rate', 'updated_by', 'updated_at',)
    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at',)

    fieldsets = ((
                     None, {
                         'fields': ('currency', 'apply_date', 'rate',)
                     }), (
                     'Other Information', {
                         'fields': ('created_at', 'created_by', 'updated_at', 'updated_by',),
                         'classes': ('collapse',)
                     })
    )

    def get_currency(self, obj):
        return obj.currency.code

    get_currency.admin_order_field = 'currency'
    get_currency.short_description = 'Currency'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        update_rate = Currency.objects.get(pk=obj.currency.id)
        update_rate.calculate()


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
