from django.contrib import admin
from .models import Product
from users.models import UserProfile


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product)
admin.site.register(UserProfile)