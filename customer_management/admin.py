from customer_management.models import Customer
from customer_management import views
from django.contrib import admin

from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _
 
class ReadOnlyModelAdmin(admin.ModelAdmin):
     
    def has_view_permission(self, request, obj=None):
        opts = self.opts
        view_permission = 'view_%s' % self.model._meta.module_name
        return request.user.has_perm(opts.app_label + '.' + view_permission)
#        return request.user.has_perm(view_permission)
     
    def has_change_permission(self, request, obj=None):
        if hasattr(self, 'is_in_change_view'):
            if self.is_in_change_view:
                return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)
        if self.has_view_permission(request, obj):
            return True
        return False
         
    def get_model_perms(self, request):
        value = super(ReadOnlyModelAdmin, self).get_model_perms(request)
        value['view'] = self.has_view_permission(request)
        return value
     
#    def changelist_view(self, request, extra_context=None):
#        result = super(ReadOnlyModelAdmin, self).changelist_view(request, extra_context)
#        return result
    
    def change_view(self, request, extra_context=None):
        self.is_in_change_view = True
        ret = None
        try:
            ret = super(ReadOnlyModelAdmin, self).change_view(request, extra_context)
        except PermissionDenied:
            self.is_in_change_view = False
            raise PermissionDenied
        return ret


def print_customers_use_lht(modeladmin, request, queryset):
    return views.print_customers_use_lht(request, queryset)
    
print_customers_use_lht.short_description = _('Print selected customers using LHT')

def print_customers_use_sf(modeladmin, request, queryset):
    return views.print_customers_use_sf(request, queryset)

print_customers_use_sf.short_description = _('Print selected customers using SF')

def print_customers_use_suer(modeladmin, request, queryset):
    return views.print_customers_use_suer(request, queryset)

print_customers_use_suer.short_description = _('Print selected customers using SUER')
    

class CustomerAdmin(ReadOnlyModelAdmin):
    list_display = ('code', 'company_name')
    search_fields = ['code', 'company_name', 'contact', 'addr', 'fax']
    actions = [print_customers_use_lht, 
               print_customers_use_sf, 
               print_customers_use_suer]
    
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
    
admin.site.register(Customer, CustomerAdmin)
