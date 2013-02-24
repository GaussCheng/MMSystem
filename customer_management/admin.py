from customer_management.models import Customer
from customer_management import views
from django.contrib import admin
from utils.readonly_model_admin import ReadOnlyModelAdmin
from django.utils.translation import ugettext as _


class CustomerAdmin(ReadOnlyModelAdmin):
    list_display = ('code', 'company_name')
    search_fields = ['code', 'company_name', 'contact', 'addr', 'fax']
    actions = ['print_customers_use_lht', 
               'print_customers_use_sf', 
               'print_customers_use_suer']
    
    def print_customers_use_lht(self, request, queryset):
        return views.print_customers_use_lht(request, queryset)
    print_customers_use_lht.short_description = _('Print selected customers using LHT')
    
    def print_customers_use_sf(self, request, queryset):
        return views.print_customers_use_sf(request, queryset)
    print_customers_use_sf.short_description = _('Print selected customers using SF')
    
    def print_customers_use_suer(self, request, queryset):
        return views.print_customers_use_suer(request, queryset)
    print_customers_use_suer.short_description = _('Print selected customers using SUER')
    
    def get_list_display(self, request):
        ret_list_display = ['code', 'company_name']
        current_user = request.user
        if current_user.has_perm('view_contact'):
            ret_list_display.append('contact')
        if current_user.has_perm('view_addr'):
            ret_list_display.append('addr')
        if current_user.has_perm('view_tel'):
            ret_list_display.append('tel')
        if current_user.has_perm('view_phone'):
            ret_list_display.append('phone')
        if current_user.has_perm('view_fax'):
            ret_list_display.append('fax')
        return ret_list_display
    
    def get_actions(self, request):
        ret_actions = super(CustomerAdmin, self).get_actions(request)
        if not request.user.has_perm("print_express_info"):
            if 'print_customers_use_lht' in ret_actions:
                del ret_actions['print_customers_use_lht']
            if 'print_customers_use_sf' in ret_actions:
                del ret_actions['print_customers_use_sf']
            if 'print_customers_use_suer' in ret_actions:
                del ret_actions['print_customers_use_suer']
        return ret_actions
    
admin.site.register(Customer, CustomerAdmin)
