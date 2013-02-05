from django.db import models
from customer_management.models import Customer
from product_management.models import Product, BugType
from express_management.models import ExpressDelivery
from django.utils.translation import ugettext_lazy as _

class MaintainLog(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=_('Customer'))
    product = models.ForeignKey(Product, verbose_name=_('Product'))
    code = models.CharField(_('Maintain Code'), max_length=50)
    manufacture_date = models.DateField(_('Manufacture Date'))
    carry_date = models.DateField(_('Carry Date'))
    bug_find_by_customer = models.TextField(_('Bug Found By Customer'))
    result = models.TextField(_('Maintain Result'))
    maintain_date = models.DateField(_('Maintain Date'))
    receive_express_number = models.CharField(_('Receive Express Number'), 
                                              max_length=50)
    invoice_number = models.CharField(_('Invoice Number'), max_length=50)
    express = models.ForeignKey(ExpressDelivery, verbose_name=_('Express Delivery'))
    
    def __unicode__(self):
        return (unicode(self.customer) + " " + 
                unicode(self.product) + " " +
                self.code)
        
    class Meta:
        verbose_name = _('Maintain Log')
        verbose_name_plural = _('Maintain Logs')
        
    def bug_type(self):
        maintain_bugs =  self.maintainbug_set.filter(maintain_log = self)
        return " : ".join(unicode(maintain_bug.bug_type) for maintain_bug in maintain_bugs)
    bug_type.short_description = _('Bug Type')
        
        
class MaintainBug(models.Model):
    maintain_log = models.ForeignKey(MaintainLog, 
                                     verbose_name=_('Maintain Log'))
    bug_type = models.ForeignKey(BugType,
                                 verbose_name=_('Bug Type'))
    description = models.TextField(_('Description'))
    
    def __unicode__(self):
        return unicode(self.maintain_log) + " : " + unicode(self.bug_type)

        
