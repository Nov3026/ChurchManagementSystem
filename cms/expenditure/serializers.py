from rest_framework import serializers
from .models import ExpenseType, Expenditure



class ExpenseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseType
        fields = ('id','name', 'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')


class ExpenditureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenditure
        fields = ('id','expenses_type', 'item','lrd_amount', 'usd_amount', 'description',
                  'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')
