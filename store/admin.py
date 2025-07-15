from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'created_date', 'updated_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    list_filter = ('is_available', 'category')
    search_fields = ('product_name', 'description')

admin.site.register(Product, ProductAdmin)