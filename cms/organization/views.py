from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Organization
from .serializers import OrganizationSerializer

# Create your views here.
class OrganizationListView(APIView):
    serializer_class = OrganizationSerializer

    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrganizationDetailView(APIView):
#     serializer_class = OrganizationSerializer

#     def get_organization(self,pk):
#         try:
#             return Organization.objects.get(pk=pk)
#         except Organization.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         organization=self.get_organization(pk)
#         serializer = OrganizationSerializer(organization)
#         return Response (serializer.data)
    
#     def put(self, request, pk):
#         organization=self.get_organization(pk)
#         serializer = OrganizationSerializer(organization,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request,pk):
#         organization=self.get_organization(pk)
#         organization.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)

class OrganizationDetailView(APIView):
    serializer_class = OrganizationSerializer

    def get_organization(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        organization = self.get_organization(pk)
        serializer = self.serializer_class(organization)
        return Response(serializer.data)

    def put(self, request, pk):
        organization = self.get_organization(pk)
        serializer = self.serializer_class(organization, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # Return detailed error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        organization = self.get_organization(pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

