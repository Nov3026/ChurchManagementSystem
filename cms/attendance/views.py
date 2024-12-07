from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import ChurchServiceAttendance, ChoirAttendance
from .serializers import ChurchServiceAttendanceSerializer, ChoirAttendanceSerializer

# Create your views here.
class ChurchServiceAttendanceListView(APIView):
    serializer_class =ChurchServiceAttendanceSerializer

    def get(self, request):
        attendees = ChurchServiceAttendance.objects.all()
        serializer =ChurchServiceAttendanceSerializer(attendees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ChurchServiceAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ChurchServiceAttendanceDetailView(APIView):
    serializer_class = ChurchServiceAttendanceSerializer

    def get_attendance(self,pk):
        try:
            return ChurchServiceAttendance.objects.get(pk=pk)
        except ChurchServiceAttendance.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        attendee = self.get_attendance(pk)
        serializer = self.serializer_class(attendee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        attendee = self.get_attendance(pk)
        serializer = self.serializer_class(attendee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        attendee = self.get_attendance(pk)
        attendee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ChoirAttendanceListView(APIView):
    serializer_class =ChoirAttendanceSerializer

    def get(self, request):
        attendees = ChoirAttendance.objects.all()
        serializer =ChoirAttendanceSerializer(attendees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ChoirAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
