from django.urls import path
from .import views


urlpatterns = [
    path('api/members/', views.MemberListView.as_view()),
    path('api/members/<int:pk>/', views.MemberDetailView.as_view()),
]
