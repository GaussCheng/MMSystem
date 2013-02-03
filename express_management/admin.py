from express_management.models import ExpressDelivery
from django.contrib import admin

class ExpressDeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel')

admin.site.register(ExpressDelivery, ExpressDeliveryAdmin)