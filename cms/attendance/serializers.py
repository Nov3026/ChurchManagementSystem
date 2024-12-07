from rest_framework import serializers
from .models import ChoirAttendance, ChurchServiceAttendance



class ChurchServiceAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChurchServiceAttendance
        fields =('id', 'activity', 'men', 'women', 'children1', 'children2', 'vistor',
                  'total_attendees','created_by', 'created_on', 'modified_on')
        read_only_fields =('total_attendees','created_by', 'created_on', 'modified_on')

class ChoirAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChoirAttendance
        fields =('id', 'activity', 'member','day', 'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')