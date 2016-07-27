from django.contrib import admin
from .models import Product,MyProducts, Thumbnail
# Register your models here.

class ThumbnailInline(admin.TabularInline):
    model = Thumbnail
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ['user','__unicode__','price']
    search_fields = ['title']
    list_filter = ['price']
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)
#admin.site.register(Thumbnail)
admin.site.register(MyProducts)
