from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}  # Automatically populate the slug field based on the name
    list_display = ('category_name', 'slug')  # Display these fields in the admin list view

admin.site.register(Category, CategoryAdmin)