from django.urls import path
from .import views


urlpatterns = [
    path('api/church_attendance/', views.ChurchServiceAttendanceListView.as_view()),
    path('api/church_attendance/<int:pk>/', views.ChurchServiceAttendanceDetailView.as_view()),

    path('api/church_attendance/', views.ChoirAttendanceListView.as_view()),
    path('api/church_attendance/<int:pk>/', views.ChurchServiceAttendanceDetailView.as_view()),
]
