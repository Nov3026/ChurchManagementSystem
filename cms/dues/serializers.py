from rest_framework import serializers
from .models import MemberDue
from datetime import date


class MemberDueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberDue
        fields = ('id', 'member', 'amount_due', 'amount_paid', 'date_paid',
                  'balance', 'created_by','created_on', 'modified_on')
        read_only_fields = ('balance', 'created_by','created_on', 'modified_on')

    def validate_date_paid(self, value):
        if value > date.today():
            raise serializers.ValidationError("Payment date cannot be in the future.")
        return value
    
    def validate(self, data):
        amount_due = data.get('amount_due')
        amount_paid = data.get('amount_paid')

        if amount_paid > amount_due:
            raise serializers.ValidationError("Amount paid cannot be greater than the amount due.")
        
        return data