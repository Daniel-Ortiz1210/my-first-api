from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from rest_framework.response import Response
from .serializers import VideoSerializer, VideoSerializerPost
from rest_framework import status


# Create your views here.
class ListVideo(APIView):
    http_method_names = ['get', 'head', 'post']
    serializer_class = VideoSerializerPost
    
    def get(self, request, format=None):
        videos = Video.objects.all()
        serialized_videos = VideoSerializer(videos, many=True)
        return Response(serialized_videos.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            slug = serializer._validated_data.get('slug')
            try:
                new_video = Video.objects.create(title=title, description=description, slug=slug)
                new_video.save()
            except:
                print('No creado')
            return Response({
                'title': title,
                'description': description,
                'slug': slug
                }, status=status.HTTP_201_CREATED)


class DetailVideo(APIView):

    def get_object(self, pk):
        video = Video.objects.filter(pk=pk).first()
        if video is None:
            raise Http404
        return video
    # http_method_names = ['get', 'head', 'post', 'put', 'delete']

    def get(self, request, pk):
        video = self.get_object(pk)
        video_serializer = VideoSerializer(video)
        return Response(video_serializer.data)
    
    def put(self, request, pk):
        video = self.get_object(pk)
        serialized_video = VideoSerializer(video, data=request.data)
        if serialized_video.is_valid():
            serialized_video.save()
        return Response(serialized_video.data)
    
    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)