from django.db import models
from django.utils.translation import ugettext_lazy as _
class ExpressDelivery(models.Model):
    name = models.CharField(_('Express Name'), max_length=50)
    tel = models.CharField(_('Tel'), max_length=15, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Express Delivery Company')
        verbose_name_plural = _('Express Delivery Companys')