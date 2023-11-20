from django.db import models
from django.utils.translation import gettext_lazy as _
 

 

class ProductTag(models.Model):
    """
    Product tag model.
    """

    id = models.PositiveBigIntegerField(_("ID"), primary_key=True)

    name = models.TextField(_("Name"))

    class Meta:
        verbose_name = _("Product Tag")
        verbose_name_plural = _("Product Tags")

    def __str__(self):
        return self.name
