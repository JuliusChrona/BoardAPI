from django.contrib import admin

from board_api.models import Post, Comment, Upvote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"link": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    pass
