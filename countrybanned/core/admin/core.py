from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from countrybanned.core.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Details'), {
            'fields': (
                'name',
                'c_index',
            ),
        }),
    )

    search_fields = ('name',)

    list_display = ('name', 'c_index')

    list_filter = ('name', 'c_index')

    ordering = ('id',)

