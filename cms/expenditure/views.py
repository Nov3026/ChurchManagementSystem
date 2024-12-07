from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import ExpenseType, Expenditure
from .serializers import ExpenseTypeSerializer, ExpenditureSerializer


# Create your views here.
class ExpenseTypeListView(APIView):
    serializer_class = ExpenseTypeSerializer

    def get(self, request):
        expenses = ExpenseType.objects.all()
        serializer = ExpenseTypeSerializer(expenses, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExpenseTypeDetailView(APIView):
    serializer_class = ExpenseTypeSerializer

    def get_expense(self,pk):
        try:
            return ExpenseType.objects.get(pk=pk)
        except ExpenseType.DoesNotExist:
            raise Http404
        
    def get(self, request,pk):
        expense = self.get_expense(pk)
        serializer = self.serializer_class(expense)
        return Response(serializer.data)
    
    def put(self,request,pk):
        expense = self.get_expense(pk)
        serializer = self.serializer_class(expense, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        expense = self.get_expense(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenditureListView(APIView):
    serializer_class = ExpenditureSerializer

    def get(self, request):
        expenses = Expenditure.objects.all()
        serializer = ExpenditureSerializer(expenses, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenditureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExpenditureDetailView(APIView):
    serializer_class = ExpenditureSerializer

    def get_expense(self,pk):
        try:
            return Expenditure.objects.get(pk=pk)
        except Expenditure.DoesNotExist:
            raise Http404
        
    def get(self, request,pk):
        expense = self.get_expense(pk)
        serializer = self.serializer_class(expense)
        return Response(serializer.data)
    
    def put(self,request,pk):
        expense = self.get_expense(pk)
        serializer = self.serializer_class(expense, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        expense = self.get_expense(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)