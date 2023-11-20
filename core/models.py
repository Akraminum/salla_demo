from django.db import models
from django.utils.translation import gettext_lazy as _


# add time stamped model
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, db_index=True, editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, db_index=True, editable=False)

    class Meta:
        abstract = True