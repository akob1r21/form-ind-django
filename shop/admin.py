from django.contrib import admin
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Product.all_objects.all()