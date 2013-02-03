from django.db import models
from customer_management.models import Customer
from product_management.models import Product
from express_management.models import ExpressDelivery

class MaintainLog(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    code = models.CharField(max_length=50)
    manufacture_date = models.DateField()
    carry_date = models.DateField()
    bug_find_by_customer = models.TextField()
    bug_find_by_tester = models.TextField()
    result = models.TextField()
    maintain_date = models.DateField()
    receive_express_number = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=50)
    express = models.ForeignKey(ExpressDelivery)
    
    def __unicode__(self):
        return (unicode(self.customer) + " " + 
                unicode(self.product) + " " +
                self.code)
        
