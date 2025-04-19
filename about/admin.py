# about/admin.py

from django.contrib import admin
from .models import SpecialMachinery, Certification

@admin.register(SpecialMachinery)
class SpecialMachineryAdmin(admin.ModelAdmin):
   list_display = ('name', 'description')
   search_fields = ('name',)
   ordering = ('name',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
   list_display = ('name', 'provider', 'date')
   search_fields = ('name', 'provider')
   ordering = ('-date',)
