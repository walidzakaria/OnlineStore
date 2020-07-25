from django.contrib import admin
from .models import Brand, Category, SubCategory, Product
from apps.authapp.models import User
from .forms import ProductForm


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_category',)
    list_filter = ('category__name',)
    search_fields = ('name', 'category__name',)

    # to refer to a foreign key
    def get_category(self, obj):
        return obj.category.name

    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category Name'


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price1', 'price2', 'description',)
#     # list_filter = ('sub_category__name', 'sub_category__category__name',)
#     # search_fields = ('sub_category__name', 'sub_category__category__name',)
#
#     # # to refer to sub category
#     # def get_sub_category(self, obj):
#     #     return obj.subcategory.name
#     #
#     # # def get_category(self, obj):
#     # #     return obj.subcategory__category.name
#     #
#     # get_sub_category.admin_order_field = 'subcategory'
#     # get_sub_category.short_description = 'Sub-Category'
#     # get_category.admin_order_field = 'category'
#     # get_category.short_description = 'Category'
#
#
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    list_display = ('id', 'name', 'brand', 'sub_category', 'price1',
                    'price2', 'updated_by', 'updated_at',)
    # prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at',)
    fieldsets = ((
                     None, {
                         'fields': ('name', 'brand', 'sub_category', 'price1', 'price2', 'description',)
                     }), (
                     'Other Information', {
                         'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',),
                         'classes': ('collapse',)
                     })
    )
    list_filter = ('sub_category__name', 'sub_category__category__name', 'brand__name',)
    search_fields = ('sub_category__name', 'sub_category__category__name', 'brand__name',)

    # to refer to sub category
    def get_sub_category(self, obj):
        return obj.subcategory.name

    def get_brand(self, obj):
        return obj.brand.name

    get_sub_category.admin_order_field = 'sub_category'
    get_sub_category.short_description = 'Sub Category'
    get_brand.admin_order_field = 'brand'
    get_brand.short_description = 'Brand'

    def save_model(self, request, obj, form, change):
        print('change: ', change)
        print('ojb: ', obj)
        print('self: ', self)
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
