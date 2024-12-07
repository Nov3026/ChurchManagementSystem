from django.urls import path
from .import views


urlpatterns = [
    path('api/expensetypes/', views.ExpenseTypeListView.as_view()),
    path('api/expensetypes/<int:pk>/', views.ExpenseTypeDetailView.as_view()),

    path('api/expenditures/', views.ExpenditureListView.as_view()),
    path('api/expenditures/<int:pk>/', views.ExpenditureDetailView.as_view())
]
