from rest_framework import serializers
from .models import Tithe
from datetime import date



class TitheSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tithe
        fields = ('id', 'member', 'lrd_amount', 'usd_amount', 'payment_date', 
                  'created_by', 'created_on', 'modified_on')
        read_only_fields =('created_by', 'created_on', 'modified_on')

    
    def validate_payment_date(self, value):
        if value > date.today():
            raise serializers.ValidationError('Payment date cannot be in the future.')
        return value
    