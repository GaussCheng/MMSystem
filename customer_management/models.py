from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    code = models.CharField(verbose_name=_('Code'), max_length=10, primary_key=True)
    company_name = models.CharField(_('Company Name'), max_length=100)
    addr = models.CharField(_('Contact Address'), max_length=200)
    contact = models.CharField(_('Contact'), max_length=20)
    tel = models.CharField(_('Telephone'), max_length=13)
    phone = models.CharField(_('Mobile'), max_length=15)
    email = models.EmailField(_('Email'), blank=True)
    
    def __unicode__(self):
        return self.code + " : " + self.company_name
    
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')