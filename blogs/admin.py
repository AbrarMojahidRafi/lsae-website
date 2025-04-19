# blogs/admin.py

from django.contrib import admin
from .models import Blog, BlogImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1
    max_num = 10

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'status')
    inlines = [BlogImageInline]
    search_fields = ('title', 'author')
    ordering = ('-published_date',)
    list_filter = ('status',)
    actions = ['approve_blogs']

    def approve_blogs(self, request, queryset):
        queryset.update(status='approved')
    approve_blogs.short_description = "Approve selected blogs"
