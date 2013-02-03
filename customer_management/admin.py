from customer_management.models import Customer
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('code', 'company_name', 'contact', 'phone')
    search_fields = ['code', 'company_name', 'contact', 'addr']
    
admin.site.register(Customer, CustomerAdmin)