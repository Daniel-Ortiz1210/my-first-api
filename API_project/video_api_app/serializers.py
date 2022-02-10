from rest_framework import serializers
from .models import Video
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializer(read_only=True)
        model = Video
        fields = (
            'id',
            'title',
            'description',
            'slug',
            'user',
            )

# curl -X POST http://localhost:8000/videos/ -H "Content-Type: application/json" -d '{"title": "video-app-2", "description": "My second video app", "slug": "new-video-2"}'

class VideoSerializerPost(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    slug = serializers.SlugField()



