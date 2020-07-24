from django.contrib import admin
from .models import User


# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone')
    list_filter = ('email',)


admin.site.register(User, AdminUser)
