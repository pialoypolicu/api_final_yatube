from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_api_v1 = DefaultRouter()
router_api_v1.register('posts', PostViewSet, basename='posts')
router_api_v1.register('group', GroupViewSet, basename='group')
router_api_v1.register(
    r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet, basename='comments'
)
router_api_v1.register('follow', FollowViewSet)
urlpatterns = [
    path('v1/', include(router_api_v1.urls))
]
