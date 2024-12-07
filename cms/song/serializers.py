from rest_framework import serializers
from .models import Song



class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ('id', 'author', 'title', 'song_content', 'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')