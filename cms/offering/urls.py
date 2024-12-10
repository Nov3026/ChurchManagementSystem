from django.urls import path
from .import views


urlpatterns = [
    path('api/offerings/', views.OfferingLIstView.as_view()),
    path('api/offerings/<int:pk>/', views.OfferingDetailView.as_view())
]
