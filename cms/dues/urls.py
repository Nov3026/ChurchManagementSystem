from django.urls import path
from .import views


urlpatterns = [
    path('api/dues/', views.MemberDueLIstView.as_view()),
    path('api/dues/<int:pk>/', views.MemberDueDetailView.as_view())
]
