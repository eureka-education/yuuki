from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from homepage.models import Post

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
