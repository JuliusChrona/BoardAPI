from django.db.models import Count, Case, When, F
from rest_framework import permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from board_api.models import Post, Upvote, Comment
from board_api.permissions import IsOwnerOrStaffOrReadOnly
from board_api.serializers import PostSerializer, UpvoteSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().annotate(
        upvote_amount=Count(Case(When(upvotes__upvote=True, then=1))),
        author_name=F("owner__username"),
    )

    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrStaffOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.validated_data["owner"] = self.request.user
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpvoteView(ModelViewSet):
    queryset = Upvote.objects.all().annotate(upvoted_user=F("user__username"))
    serializer_class = UpvoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user

        if not self.validate(serializer):
            serializer.save()
        else:
            error_message = {"post": ["post with this user already exists"]}
            raise ValidationError(error_message)

    def validate(self, serializer):
        is_exist = Upvote.objects.filter(
            post=serializer.validated_data["post"], user=self.request.user
        ).exists()
        return is_exist


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().annotate(author_name=F("user__username"))
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.save()
