from django.urls import path
from .views import APIPost, APIPostDetail
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/v1/posts/', APIPost.as_view()),
    path('api/v1/posts/<int:id>/', APIPostDetail.as_view()),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
