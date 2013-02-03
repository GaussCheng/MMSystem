from django.db import models
from django.utils.translation import gettext_lazy as _

class BugType(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Bug Types')
        verbose_name_plural = _('Bug Types')
    
class Product(models.Model):
    model = models.CharField(max_length=50)
    display = models.CharField(max_length=50, blank=True)
    version = models.CharField(max_length=50)
    release_time = models.DateField(blank=True)
    bug_types = models.ManyToManyField(BugType, blank=True)
    
    class Meta:
        unique_together = ('model', 'version')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    
    
    def __unicode__(self):
        return self.model + " : " + self.version

