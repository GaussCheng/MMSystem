from django.db import models

class ExpressDelivery(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name