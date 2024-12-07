from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .serializers import  MemberSerializer
# from django.contrib.auth.models import User
from .models import Member
from rest_framework.views import APIView



class MemberListView(APIView):
    serializer_class = MemberSerializer

    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class MemberDetailView(APIView):
    serializer_class = MemberSerializer

    def get_member(self,pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        member = self.get_member(pk)
        serializer = self.serializer_class(member)
        return Response(serializer.data)
    
    def put(self,request,pk):
        member = self.get_member(pk=pk)
        serializer = self.serializer_class(member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        member = self.get_member(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





