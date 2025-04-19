# home/admin.py

from django.contrib import admin
from .models import ProductLine, Enquiry

@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'enquiry_for', 'message', 'sent_at')
    search_fields = ('name', 'email', 'enquiry_for__name')
    list_filter = ('enquiry_for', 'sent_at')
    ordering = ('-sent_at',)
