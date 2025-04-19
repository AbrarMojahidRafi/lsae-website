# gallery/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_line', 'description', 'details')
    search_fields = ('name', 'product_line__name')
    ordering = ('name',)
