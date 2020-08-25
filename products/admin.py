from django.contrib import admin

# Register your models here.
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

