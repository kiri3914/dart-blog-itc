from django.shortcuts import render
from .models import Category, Tag, Post
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F

class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_context_data(self,*args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My first blog"
        return context

class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self,*args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context