from rest_framework import serializers

from board_api.models import Post, Upvote, Comment


class PostSerializer(serializers.ModelSerializer):
    upvote_amount = serializers.ReadOnlyField()
    author_name = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "upvote_amount",
            "creation_date",
            "author_name",
        )


class UpvoteSerializer(serializers.ModelSerializer):
    upvoted_user = serializers.CharField(read_only=True)

    class Meta:
        model = Upvote
        fields = ("upvoted_user", "post", "upvote")


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author_name = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ("post", "author_name", "content", "creation_date")
