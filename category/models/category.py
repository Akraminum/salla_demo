from django.db import models
from django.utils.translation import gettext_lazy as _

from merchants.models import Merchant


class Category(models.Model):
    STATUS = (
        ('active', 'Active'),
        ('visible', 'Visible'),
        ('hidden', 'Hidden')
    )

    id = models.BigIntegerField(primary_key=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.DO_NOTHING, 
        related_name='subs',
        null=True, blank=True)
     
    merchant = models.ForeignKey(
        Merchant,
        verbose_name=_("Merchant"),
        related_name="categories",
        on_delete=models.CASCADE,
    )
    
    name = models.CharField(max_length=100)
    sort_order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='hidden')
    update_at = models.DateTimeField()
    
    metadata_title = models.CharField(max_length=255, blank=True, null=True)
    metadata_description = models.TextField(blank=True, null=True)
    metadata_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    




