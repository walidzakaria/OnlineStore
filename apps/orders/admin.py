from django.contrib import admin
from django.db.models import Sum

from .forms import PurchaseForm, OrderForm, OrderItemsForm
from apps.currencies.models import ExchangeRate


# Register your models here.
from .models import Purchase, Order, UserAddress, OrderItems
from ..products.models import Product


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

    def delete_model(self, request, obj):
        product = Product.objects.get(pk=obj.product.id)
        obj.delete()
        product.save()

    def delete_selection(self, request, obj):
        for o in obj.all():
            product = Product.objects.get(pk=o.product.id)
            o.delete()
            product.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    actions = ['delete_selection']
    delete_selection.short_description = 'Delete selected purchases'


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address',)


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ('id', 'client', 'status', 'user_address', 'notes', 'number_of_items',
                    'due_amount', 'exchanged_due_amount', 'currency',)
    readonly_fields = ('number_of_items', 'due_amount', 'created_by', 'created_at',
                       'updated_by', 'updated_at', 'exchange_rate', 'exchanged_due_amount',)
    fieldsets = (
        (None, {'fields': ('client', 'status', 'user_address', 'number_of_items', 'due_amount',
                           'currency', 'exchange_rate', 'exchanged_due_amount', 'notes')}),
        ('Other Information', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',),
            'classes': ('collapse',)
        }))
    search_fields = ('id',)
    # list_filter = ('client',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    def delete_model(self, request, obj):
        order_items = OrderItems.objects.filter(order=obj.id).all()
        for i in order_items:
            product = Product.objects.get(pk=i.product.id)
            i.delete()
            product.save()
        obj.delete()

    def delete_selection(self, request, obj):
        for o in obj.all():
            order_items = OrderItems.objects.filter(order=o.id).all()
            for i in order_items:
                product = Product.objects.get(pk=i.product.id)
                i.delete()
                product.save()
            o.delete()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    actions = ['delete_selection']
    delete_selection.short_description = 'Delete selected orders'


class OrderItemsAdmin(admin.ModelAdmin):
    form = OrderItemsForm
    list_display = ('order', 'product', 'quantity', 'price', 'product_value',)
    readonly_fields = ('price', 'product_value',)

    # to refer to a foreign key
    def price(self, obj):
        return obj.product.price1

    def delete_model(self, request, obj):
        product = Product.objects.get(pk=obj.product.id)
        order = Order.objects.get(pk=obj.order.id)
        obj.delete()
        order.save()
        product.save()

    def delete_selection(self, request, obj):
        for o in obj.all():
            product = Product.objects.get(pk=o.product.id)
            order = Order.objects.get(pk=o.order.id)
            o.delete()
            product.save()
            order.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    actions = ['delete_selection']
    delete_selection.short_description = 'Delete selected order items'


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)