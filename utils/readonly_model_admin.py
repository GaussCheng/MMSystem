from django.contrib import admin
from django.core.exceptions import PermissionDenied

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


    