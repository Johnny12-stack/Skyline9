from django.contrib import admin
from .models import Product, Profile


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product)
admin.site.register(Profile)