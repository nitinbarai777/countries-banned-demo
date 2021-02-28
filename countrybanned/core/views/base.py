import hashlib
import random
from django.db.models import Q
from django.conf import settings
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework import mixins, viewsets, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from countrybanned.core.models.core import Country

def home(request):
    from countrybanned.core.views.core import CountrySerializer
    countries = Country.objects.order_by('name').all()
    context = {'json_countries': CountrySerializer(countries, many=True).data,}
    return render(request, 'banned-countries.html', context)

