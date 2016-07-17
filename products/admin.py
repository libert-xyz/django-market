from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','price']
    search_fields = ['title']
    list_filter = ['price']
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)
