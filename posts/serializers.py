# posts > serializers.py
# 주의! DRF는 TextField를 지원하지 않음. -> CharField로 내부적으로 긴 문자열을 받을 수 있음.

from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    view_count = serializers.IntegerField()
    writer = serializers.IntegerField()
    bad_post = serializers.BooleanField()

    # create 추가
    def create(self, validated_data):
        post = Post.objects.create(
            content = validated_data['content'],
            view_count = validated_data['view_count'],
            writer = User.objects.get(id = validated_data['writer']),
        )
        return post
        # return Post.objects.create(validated_data)

# ModelSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'post', 'writer']