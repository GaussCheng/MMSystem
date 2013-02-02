from django.db import models

class Customer(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    company_name = models.CharField(max_length=100)
    addr = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    tel = models.CharField(max_length=13)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.code + " : " + self.company_name