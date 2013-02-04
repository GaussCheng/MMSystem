# -*- coding: utf-8 -*-

from maintain_log.models import MaintainLog, MaintainBug
from django.contrib import admin
from django.utils.translation import ugettext as _

class MaintainBugInline(admin.StackedInline):
    model = MaintainBug
    extra = 1
    verbose_name = _('Maintain Bug')
    verbose_name_plural = _('Maintain Bugs')

class MaintainLogdmin(admin.ModelAdmin):
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
    
    list_display = ('code', 'product', 'customer', 'carry_date')
    list_filter = ['carry_date', 'maintain_date']
    search_fields = ['bug_find_by_customer', 'result']
    
admin.site.register(MaintainLog, MaintainLogdmin)