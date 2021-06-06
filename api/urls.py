from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_api_v1 = DefaultRouter()
router_api_v1.register('posts', PostViewSet, basename='posts')
router_api_v1.register('group', GroupViewSet, basename='group')
router_api_v1.register(
    r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet, basename='comments'
)
router_api_v1.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]
