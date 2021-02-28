from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from countrybanned.core.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Details'), {
            'fields': (
                'name',
            ),
        }),
    )

    search_fields = ('name',)

    list_display = ('name',)

    list_filter = ('name',)

    ordering = ('id',)

