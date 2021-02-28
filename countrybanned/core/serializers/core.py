from rest_framework import serializers
from countrybanned.core.models.core import Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"
