from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .serializers import GroupSerializer, GroupExtensionSerializer
from .models import GroupExtension


# Create your views here.
class GroupListView(APIView):
    serializer_class = GroupSerializer
    
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetailView(APIView):
    serializer_class = GroupSerializer
    
    def get_group(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        group = self.get_group(pk)
        serializer = self.serializer_class(group)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        group = self.get_group(pk)
        serializer = self.serializer_class(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        group = self.get_group(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupExtensionListView(APIView):
    serializer_class = GroupExtensionSerializer

    def get(self, request):
        group_extensions = GroupExtension.objects.all()
        serializer = GroupExtensionSerializer(group_extensions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupExtensionDetailView(APIView):
    serializer_class = GroupExtensionSerializer

    def get_group_extension(self, pk):
        try:
            return GroupExtension.objects.get(pk=pk)
        except GroupExtension.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        group_extension = self.get_group_extension(pk)
        serializer = self.serializer_class(group_extension)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        group_extension = self.get_group_extension(pk)
        serializer = self.serializer_class(group_extension, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        group_extension = self.get_group_extension(pk)
        group_extension.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)