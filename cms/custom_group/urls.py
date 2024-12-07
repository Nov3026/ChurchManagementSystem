from django.urls import path
from .import views


urlpatterns = [
    path('api/groups/', views.GroupListView.as_view()),
    path('api/groups/<int:pk>/', views.GroupDetailView.as_view()),

    path('api/custom_groups/', views.GroupExtensionListView.as_view()),
    path('api/custom_groups/<int:pk>/', views.GroupExtensionDetailView.as_view()),
]
