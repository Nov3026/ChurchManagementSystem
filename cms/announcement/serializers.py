from rest_framework import serializers
from .models import Announcement



class AnnouncementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Announcement
        fields = ('id', 'author', 'title', 'content', 'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')