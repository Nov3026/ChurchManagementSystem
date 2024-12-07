from django.urls import path
from . import views


urlpatterns = [
    path('api/organizations/', views.OrganizationListView.as_view()),
    path('api/organizations/<int:pk>/', views.OrganizationDetailView.as_view())
]
