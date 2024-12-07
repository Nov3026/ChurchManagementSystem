from django.urls import path
from .import views


urlpatterns = [
    path('api/songs/', views.SongListView.as_view()),
    path('api/songs/<int:pk>/', views.SongDetailView.as_view())
]
