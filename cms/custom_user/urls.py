from django.urls import path
from .import views


urlpatterns = [
    path('api/users/', views.CustomUserListView.as_view()),
    path('api/users/<int:pk>/', views.CustomUserDetailView.as_view()),
]
