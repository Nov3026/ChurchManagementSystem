from rest_framework import serializers
from .models import Content, ContentType


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = ('id', 'name', 'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('id', 'content_type','title', 'description', 'photo_url', 'created_by', 'created_on', 'modified_on')
        read_only_fields = ('created_by', 'created_on', 'modified_on')