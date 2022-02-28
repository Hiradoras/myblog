from dataclasses import fields
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post # this Post is the object that we can use in html. 
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
    #fields = ('title', 'body')