from django.urls import path
from .import views


urlpatterns = [
    path('api/activities/', views.ActivityListView.as_view()),
    path('api/activities/<int:pk>/', views.ActivityDetailView.as_view()),
]
