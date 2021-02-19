from django.urls import path, include
from rest_framework.routers import SimpleRouter

from board_api.views import PostViewSet, UpvoteView, CommentViewSet

router = SimpleRouter()

router.register(r"post", PostViewSet)
router.register(r"post_upvote", UpvoteView)
router.register(r"comment", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
