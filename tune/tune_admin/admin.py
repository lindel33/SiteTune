from django.contrib import admin

from .models import Product, Category


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'sell', 'day_created', ]


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', ]