from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    company_name = models.CharField(max_length=100)
    addr = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    tel = models.CharField(max_length=13)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.code + " : " + self.company_name
    
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')