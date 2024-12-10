from rest_framework import serializers
from .models import Offering
from datetime import date


class OfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offering
        fields = ('id', 'offering_type', 'lrd', 'usd','created_by','created_on', 'modified_on')
        read_only_fields = ('created_by','created_on', 'modified_on')