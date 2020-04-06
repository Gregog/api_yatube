from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'post', 'text', 'created')
        model = Comment