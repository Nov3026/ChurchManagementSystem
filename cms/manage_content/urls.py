from django.urls import path
from .import views


urlpatterns = [
    path('api/content_types/', views.ContentTypeListView.as_view()),
    path('api/content_types/<int:pk>/', views.ContentTypeDetailView.as_view()),

    path('api/contents/', views.ContentListView.as_view()),
    path('api/contents/<int:pk>/', views.ContentDetailView.as_view())
]
