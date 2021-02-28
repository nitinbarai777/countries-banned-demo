from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
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


@receiver(pre_save, sender=Country)
def pre_save_Country(sender, instance, **kwargs):

    print('===>>>> pre_save_Country')
    instance.c_index = instance.name[0].capitalize()
