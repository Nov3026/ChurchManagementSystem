from django.shortcuts import render
from .serializers import MemberDueSerializer
from .models import MemberDue
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


# Create your views here.
class MemberDueLIstView(APIView):
    serializer_class = MemberDueSerializer

    def get(self, request):
        due = MemberDue.objects.all()
        serializer = MemberDueSerializer(due, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MemberDueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MemberDueDetailView(APIView):
    serializer_class = MemberDueSerializer

    def get_due(self,pk):
        try:
            return MemberDue.objects.get(pk=pk)
        except MemberDue.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        due = self.get_due(pk)
        serializer = MemberDueSerializer(due)
        return Response(serializer.data)
    
    def put(self,request,pk):
        due = self.get_due(pk=pk)
        serializer = MemberDueSerializer(due, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        due = self.get_due(pk)
        due.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





