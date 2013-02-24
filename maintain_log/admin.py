# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms
from utils.readonly_model_admin import ReadOnlyModelAdmin
from maintain_log import views
from maintain_log.models import MaintainLog, MaintainBug

class MaintainBugForm(forms.ModelForm):
    bug_types = None
    def __init__(self, *args, **kwargs):
        super(MaintainBugForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            MaintainBugForm.bug_types = self.instance.maintain_log.product.bug_types.all()
            bug_type_field = self.fields['bug_type']
            bug_type_field.queryset = MaintainBugForm.bug_types
    class Meta:
        model = MaintainBug
        
class MaintainBugInline(admin.StackedInline):
    model = MaintainBug
    extra = 1
    verbose_name = _('Maintain Bug')
    verbose_name_plural = _('Maintain Bugs')
#    form = MaintainBugForm
#    raw_id_fields = ['bug_type']


class MaintainLogAdmin(ReadOnlyModelAdmin):
    save_on_top = True
    raw_id_fields = ['customer']
    actions = ["print_data", "export_to_excel"]
    fieldsets = [
        (None,   {'fields': ['code']}),
        (_('Product Information'), {'fields': ['product', 'manufacture_date']}),
        (_('Customer Information'), {'fields': ['customer']}),
        (_('Maintain Information'), {'fields': ['carry_date', 'bug_find_by_customer',
                                          'result', 'maintain_date']}),
        (_('Invoice Information'), {'fields': ['receive_express', 'receive_express_number', 
                                          'invoice_number', 'express']})
    ]
    inlines = [MaintainBugInline]
    
    
    list_display = ('code', 
                    'product', 
                    'customer',
                    'bug_find_by_customer', 
                    'bug_type', 
                    'carry_date',
                    'maintain_date',
                    'result')
    list_filter = ['product__model', 
                   'product__version',
                   'customer__company_name',
                   'maintainbug__bug_type',
                   'carry_date', 
                   'maintain_date']
    search_fields = ['product__model', 
                     '^product__version',
                     '^customer__code',
                     'customer__company_name',
                     'bug_find_by_customer',
                     'maintainbug__description',
                     'code',
                     'result']
    date_hierarchy = 'maintain_date'
    
    def print_data(self, request, queryset):
        return views.print_to_html(request, queryset)
    print_data.short_description = _('Print selected data')
    
    def export_to_excel(self, request, queryset):
        return views.export_to_excel(request, queryset)
    export_to_excel.short_description = _('Export to excel')
    
    def get_list_display(self, request):
        ret_list_display = self.list_display
        current_user = request.user
        if not current_user.has_perm('view_result'):
            if "result" in ret_list_display:
                del ret_list_display
        return ret_list_display
    
    def get_actions(self, request):
        ret_actions = super(MaintainLogAdmin, self).get_actions(request)
        if not request.user.has_perm("print_log"):
            if 'print_data' in ret_actions:
                del ret_actions['print_data']
        if not request.user.has_perm("export_log"):
            if 'export_to_excel' in ret_actions:
                del ret_actions['export_to_excel']
        return ret_actions
    
admin.site.register(MaintainLog, MaintainLogAdmin)
