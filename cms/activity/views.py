from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .serializers import ActivitySerializer
from .models import Activity

# Create your views here.
class ActivityListView(APIView):
    serializer_class = ActivitySerializer

    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ActivityDetailView(APIView):
    serializer_class = ActivitySerializer

    def get_activity(self,pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        activity = self.get_activity(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    def put(self,request,pk):
        activity = self.get_activity(pk)
        serializer = ActivitySerializer(activity,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        activity = self.get_activity(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
