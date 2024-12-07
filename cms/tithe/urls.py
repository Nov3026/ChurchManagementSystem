from django.urls import path
from .import views


urlpatterns = [
    path('api/tithes/', views.TitheListView.as_view()),
    path('api/tithes/<int:pk>/', views.TitheDetailView.as_view()),
]
