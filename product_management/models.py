from django.db import models

class Product(models.Model):
    model = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    release_time = models.DateField
    
    class Meta:
        unique_together = ('model', 'version')
    
    
    def __unicode__(self):
        return self.model + " : " + self.version
