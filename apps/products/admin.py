from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Brand, Category, SubCategory, Product, Review, Slider
from apps.authapp.models import User
from .forms import ProductForm, ReviewForm, SliderForm


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_ar',)
    list_filter = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_ar',)
    list_filter = ('name',)
    search_fields = ('name', 'name_ar')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_ar', 'get_category',)
    list_filter = ('category__name',)
    search_fields = ('name', 'category__name', 'name_ar')

    # to refer to a foreign key
    def get_category(self, obj):
        return obj.category.name

    def get_category_ar(self, obj):
        return obj.category.name_ar

    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category Name'
    get_category_ar.admin_order_field = 'category'
    get_category_ar.short_description = 'Category Name AR'


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    list_display = ('id', 'name', 'name_ar', 'keywords', 'brand', 'sub_category', 'price1',
                    'price2', 'delivery_days', 'updated_by', 'updated_at',
                    'purchased', 'sold', 'balance', 'number_of_reviews', 'rating_average',
                    'active',)
    # prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at',
                       'purchased', 'sold', 'balance', 'number_of_reviews', 'rating_average', 'reduction',
                       'preview_image1', 'preview_image2', 'preview_image3', 'preview_image4', 'preview_image5',)
    fieldsets = ((
                     None, {
                         'fields': (
                             'name', 'name_ar', 'keywords', 'brand', 'sub_category', 'price1', 'price2',
                             'delivery_days', 'description', 'description_ar',
                             'image1', 'image2', 'image3', 'image4', 'image5', 'preview_image1',
                             'preview_image2', 'preview_image3', 'preview_image4', 'preview_image5',
                             'active',)
                     }), (
                     'Other Information', {
                         'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',
                                    'purchased', 'sold', 'balance', 'number_of_reviews', 'rating_average',),
                         'classes': ('collapse',)
                     })
    )
    list_filter = ('active', 'sub_category__name', 'sub_category__category__name', 'brand__name',)
    search_fields = ('sub_category__name', 'sub_category__category__name',
                     'brand__name', 'name', 'name_ar', 'keywords')

    # to refer to sub category
    def get_sub_category(self, obj):
        return obj.subcategory.name

    def get_brand(self, obj):
        return obj.brand.name

    def preview_image1(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image1.url,
            width=130,
            height=130,
        ))

    def preview_image2(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image2.url,
            width=130,
            height=130,
        ))

    def preview_image3(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image3.url,
            width=130,
            height=130,
        ))

    def preview_image4(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image4.url,
            width=130,
            height=130,
        ))

    def preview_image5(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image5.url,
            width=130,
            height=130,
        ))

    get_sub_category.admin_order_field = 'sub_category'
    get_sub_category.short_description = 'Sub Category'
    get_brand.admin_order_field = 'brand'
    get_brand.short_description = 'Brand'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    list_display = ('product', 'rating', 'comment', 'updated_by', 'updated_at')
    readonly_fields = ('updated_by', 'updated_at', 'created_by', 'created_at',)
    list_filter = ('product', 'rating',)
    search_fields = ('product',)
    fieldsets = ((
                     None, {
                         'fields': ('product', 'rating', 'comment',)
                     }), (
                     'Other Information', {
                         'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',),
                         'classes': ('collapse',)
                     })
    )

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
    delete_selection.short_description = 'Delete selected reviews'


class SliderAdmin(admin.ModelAdmin):
    form = SliderForm
    list_display = ('name', 'link_field', 'updated_by', 'updated_at', 'lang', 'active')
    readonly_fields = ('updated_by', 'updated_at', 'created_by', 'created_at',
                       'preview_image', 'link_field',)
    search_fields = ('name',)
    list_filter = ('active', 'lang', )
    fieldsets = ((
                     None, {
                         'fields': ('name', 'image', 'preview_image', 'link', 'link_field', 'lang', 'active',)
                     }), (
                     'Other Information', {
                         'fields': ('created_by', 'created_at', 'updated_by', 'updated_at',),
                         'classes': ('collapse',)
                     })
    )

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}%" height={height} />'.format(
            url=obj.image.url,
            width=100,
            height=480,
        ))

    def link_field(self, obj):
        return mark_safe('<a href="{url}" target="_blank">{url}</a>'. format(
            url=obj.link
        ))

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Slider, SliderAdmin)
