from customer_management.models import Customer
from django.contrib import admin

from django.contrib.auth.models import Permission
 
 
class ReadOnlyModelAdmin(admin.ModelAdmin):
     
    def has_view_permission(self, request, obj=None):
        opts = self.opts
        view_permission = 'view_%s' % self.model._meta.module_name
        return request.user.has_perm(opts.app_label + '.' + view_permission)
     
    def has_change_permission(self, request, obj=None):
        if hasattr(self, 'has_change'):
            if self.has_change:
                return True
        return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)
         
    def get_model_perms(self, request):
        value = super(ReadOnlyModelAdmin, self).get_model_perms(request)
        value['view'] = self.has_view_permission(request)
        return value
     
    def changelist_view(self, request, extra_context=None):
        if self.has_view_permission(request, None):
            self.has_change = True
        result = super(ReadOnlyModelAdmin, self).changelist_view(request, extra_context)
        self.has_change = False
        return result


class CustomerAdmin(ReadOnlyModelAdmin):
    list_display = ('code', 'company_name')
    search_fields = ['code', 'company_name', 'contact', 'addr', 'fax']
    
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
