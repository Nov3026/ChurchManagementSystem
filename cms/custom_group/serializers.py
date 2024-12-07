from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import GroupExtension



class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('id','name')

class GroupExtensionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupExtension
        fields = ('id','group', 'organization')
