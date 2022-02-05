from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category, SeriesCategory


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'category', 'series', 'sell', 'day_created', 'next_edition', ]

    def image_show(self, obj):
        if obj.image_1:
            return mark_safe("<img src='{}' width='60' />".format(obj.image_1.url))
        return 'None'

    image_show.__name__ = "Картинка"


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', ]


@admin.register(SeriesCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', ]
