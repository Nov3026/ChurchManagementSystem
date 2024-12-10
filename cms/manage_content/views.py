from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import ContentType, Content
from .serializers import ContentTypeSerializer, ContentSerializer


# Create your views here.
class ContentTypeListView(APIView):
    serializer_class = ContentTypeSerializer

    def get(self, request):
        content_types = ContentType.objects.all()
        serializer = ContentTypeSerializer(content_types, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ContentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContentTypeDetailView(APIView):
    serializer_class = ContentTypeSerializer

    def get_content_type(self,pk):
        try:
            return ContentType.objects.get(pk=pk)
        except ContentType.DoesNotExist:
            raise Http404
        
    def get(self, request,pk):
        content_type = self.get_content_type(pk)
        serializer = ContentTypeSerializer(content_type)
        return Response(serializer.data)
    
    def put(self,request,pk):
        expense = self.get_content_type(pk)
        serializer = ContentTypeSerializer(expense, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        expense = self.get_content_type(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentListView(APIView):
    serializer_class = ContentSerializer

    def get(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ContentDetailView(APIView):
    serializer_class = ContentSerializer

    def get_content(self,pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise Http404
        
    def get(self, request,pk):
        content = self.get_content(pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data)
    
    def put(self,request,pk):
        content = self.get_content(pk)
        serializer = ContentSerializer(content, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        content = self.get_content(pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)