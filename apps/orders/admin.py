from django.contrib import admin
from django.db.models import Sum

from .forms import PurchaseForm, OrderForm, OrderItemsForm


# Register your models here.
from .models import Purchase, Order, UserAddress, OrderItems


class PurchaseAdmin(admin.ModelAdmin):
    form = PurchaseForm
    list_display = ('id', 'vendor', 'date', 'product', 'quantity', 'net_price', 'product_value',
                    'updated_by', 'created_at')
    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at', 'product_value')

    fieldsets = (
        (None, {'fields': ('vendor', 'date', 'product', 'quantity', 'net_price', 'product_value',)}),
        ('Other Information', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',),
            'classes': ('collapse',)
        }))
    search_fields = ('id',)
    list_filter = ('vendor', 'product',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address',)


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ('id', 'client', 'status', 'user_address', 'notes', 'number_of_items', 'due_amount',)
    readonly_fields = ('number_of_items', 'due_amount', 'created_by', 'created_at', 'updated_by', 'updated_at',)
    fieldsets = (
        (None, {'fields': ('client', 'status', 'user_address', 'number_of_items', 'due_amount', 'notes',)}),
        ('Other Information', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',),
            'classes': ('collapse',)
        }))
    search_fields = ('id',)
    list_filter = ('client',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


class OrderItemsAdmin(admin.ModelAdmin):
    form = OrderItemsForm
    list_display = ('order', 'product', 'quantity', 'price', 'product_value',)
    readonly_fields = ('price', 'product_value',)

    # to refer to a foreign key
    def price(self, obj):
        return obj.product.price1

    def save_model(self, request, obj, form, change):
        order = Order.objects.get(pk=obj.order.id)
        order.updated_by = request.user
        obj.calculate()
        order.calculate()


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)