# -*- coding: utf-8 -*-

from maintain_log.models import MaintainLog, MaintainBug
from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms

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

class MaintainLogdmin(admin.ModelAdmin):
    raw_id_fields = ['customer']
    fieldsets = [
        (None,   {'fields': ['code']}),
        (_('Product Information'), {'fields': ['product', 'manufacture_date']}),
        (_('Customer Information'), {'fields': ['customer']}),
        (_('Maintain Information'), {'fields': ['carry_date', 'bug_find_by_customer',
                                          'result', 'maintain_date']}),
        (_('Invoice Information'), {'fields': ['receive_express_number', 
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
    
admin.site.register(MaintainLog, MaintainLogdmin)
