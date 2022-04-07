from django.urls import path
from .views import Home, GetPost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug>', GetPost.as_view(), name='post')
]
