from product_management.models import Product, BugType
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('model', 'display', 'version', 'release_time')
    list_filter = ['release_time']

admin.site.register(Product, ProductAdmin)
admin.site.register(BugType)