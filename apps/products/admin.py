from django.contrib import admin
from .models import Brand, Category, SubCategory, Product


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


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price1', 'price2', 'description',)
    # list_filter = ('sub_category__name', 'sub_category__category__name',)
    # search_fields = ('sub_category__name', 'sub_category__category__name',)

    # # to refer to sub category
    # def get_sub_category(self, obj):
    #     return obj.subcategory.name
    #
    # # def get_category(self, obj):
    # #     return obj.subcategory__category.name
    #
    # get_sub_category.admin_order_field = 'subcategory'
    # get_sub_category.short_description = 'Sub-Category'
    # get_category.admin_order_field = 'category'
    # get_category.short_description = 'Category'


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
