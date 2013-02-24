# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Customer(models.Model):
    code = models.CharField(verbose_name=_('Code'), max_length=10, primary_key=True)
    company_name = models.CharField(_('Company Name'), max_length=100)
    addr = models.CharField(_('Contact Address'), max_length=200)
    contact = models.CharField(_('Contact'), max_length=20)
    tel = models.CharField(_('Telephone'), max_length=13)
    phone = models.CharField(_('Mobile'), max_length=15)
    fax = models.CharField(_('Fax'), max_length=15, blank=True)
    email = models.EmailField(_('Email'), blank=True)
    note = models.TextField(_('Note'), blank=True)
    
    def __unicode__(self):
        return self.code + " : " + self.company_name
    
    def class_name(self):
        return "customer"
    
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        permissions = (
            ("view_customer", _("可以查看客户")),
            ("view_contact", _("可以查看客户联系人")),
            ("view_addr", _("可以查看客户地址")),
            ("view_tel", _("可以查看客户固话")),
            ("view_phone", _("可以查看客户手机")),
            ("view_fax", _("可以查看客户传真")),
            ("view_email", _("可以查看客户邮箱"))
        )