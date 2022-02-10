from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListVideo.as_view(), name='videos'),
    path('<pk>', views.DetailVideo.as_view(), name='video'),
]