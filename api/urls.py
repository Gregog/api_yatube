from django.urls import path, include
from .views import PostViewSet, APICommentView, APICommentDetailView

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)

urlpatterns = [
    path('api/v1/posts/<int:post_id>/comments/', APICommentView.as_view()),
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/', APICommentDetailView.as_view()),
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]