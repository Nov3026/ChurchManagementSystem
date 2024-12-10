from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Tithe
from .serializers import TitheSerializer


# Create your views here.
class TitheListView(APIView):
    serializer_class = TitheSerializer

    def get(self, request):
        tithes = Tithe.objects.all()
        serializer = TitheSerializer(tithes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TitheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TitheDetailView(APIView):
    serializer_class = TitheSerializer

    def get_tithe(self,pk):
        try:
            return Tithe.objects.get(pk=pk)
        except Tithe.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        tithe = self.get_tithe(pk)
        serializer = TitheSerializer(tithe)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tithe = self.get_tithe(pk)
        serializer = TitheSerializer(tithe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tithe = self.get_tithe(pk)
        tithe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)