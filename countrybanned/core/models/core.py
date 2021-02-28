from django.utils.translation import ugettext_lazy as _
from .base import *

class Country(Base):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=200,
        null=True
    )

    c_index = models.CharField(
        verbose_name=_('Index'),
        max_length=200,
        null=True
    )

    def __str__(self):
        return self.name
