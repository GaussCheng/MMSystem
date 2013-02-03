from django.db import models
from customer_management.models import Customer
from product_management.models import Product, BugType
from express_management.models import ExpressDelivery
from django.utils.translation import gettext_lazy as _

class MaintainLog(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    code = models.CharField(max_length=50)
    manufacture_date = models.DateField()
    carry_date = models.DateField()
    bug_find_by_customer = models.TextField()
    result = models.TextField()
    maintain_date = models.DateField()
    receive_express_number = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=50)
    express = models.ForeignKey(ExpressDelivery)
    
    def __unicode__(self):
        return (unicode(self.customer) + " " + 
                unicode(self.product) + " " +
                self.code)
        
    class Meta:
        verbose_name = _('Maintain Log')
        verbose_name_plural = _('Maintain Logs')
        
        
class MaintainBug(models.Model):
    maintain_log = models.ForeignKey(MaintainLog)
    bug_type = models.ForeignKey(BugType)
    description = models.TextField()
    
    def __unicode__(self):
        return unicode(self.maintain_log) + " : " + unicode(self.bug_type)

        
