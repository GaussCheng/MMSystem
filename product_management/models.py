from django.db import models

class BugType(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
class Product(models.Model):
    model = models.CharField(max_length=50)
    display = models.CharField(max_length=50, blank=True)
    version = models.CharField(max_length=50)
    release_time = models.DateField(blank=True)
    bug_types = models.ManyToManyField(BugType, blank=True)
    
    class Meta:
        unique_together = ('model', 'version')
    
    
    def __unicode__(self):
        return self.model + " : " + self.version

