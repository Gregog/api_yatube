from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        read_only_fields = ('author',)
        model = Post

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment