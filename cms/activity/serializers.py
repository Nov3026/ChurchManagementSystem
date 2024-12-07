from rest_framework import serializers
from .models import Activity



class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'name','start_time', 'end_time', 'day', 'description','created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')