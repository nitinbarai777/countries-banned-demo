from django.utils.translation import ugettext_lazy as _
from django.db import models


# Abstract models
class Base(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name=_('Updated at')
    )

    class Meta:
        abstract = True
