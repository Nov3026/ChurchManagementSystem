from django.urls import path
from .import views


urlpatterns = [
    path('api/announcements/', views.AnnouncementListView.as_view()),
    path('api/announcements/<int:pk>/', views.AnnouncementDetailView.as_view())
]
