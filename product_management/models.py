from django.db import models
from django.utils.translation import ugettext_lazy as _

class BugType(models.Model):
    name = models.CharField(_('Type Name'), max_length=100)
    decription = models.TextField(_('Description'), blank=True)
    note = models.TextField(_('Note'))
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Bug Types')
        verbose_name_plural = _('Bug Types')
    
class Product(models.Model):
    model = models.CharField(_('Model'), max_length=50)
    display = models.CharField(_('Display Name'), max_length=50, blank=True)
    version = models.CharField(_('Version'), max_length=50)
    release_time = models.DateField(_('Release Date'), blank=True)
    bug_types = models.ManyToManyField(BugType, 
                                       blank=True, 
                                       verbose_name=_('Bug Types'))
    note = models.TextField(_('Note'))
    
    class Meta:
        unique_together = ('model', 'version')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    
    
    def __unicode__(self):
        return self.model + " : " + self.version
    
    def bound_bug_types(self):
        bugtypes = self.bug_types.all()
        return " : ".join(unicode(bug_type) for bug_type in bugtypes)
    bound_bug_types.short_description = _('Bug Types')


