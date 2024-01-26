from django.shortcuts import render
from .models import Post
from datetime import date
# Create your views here.

def get_data(post):
    return post['date']

sorted_posts = Post.objects.all().order_by('-date')
latest_posts = Post.objects.all().order_by('-date')[:3]

def starting_page(request):
    return render(request,'posts/index.html',{
        "posts":latest_posts
    })

def all_post(request):
    return render(request,'posts/all-posts.html',{
        "posts":sorted_posts
    })

def post_details(request,slug):
    specific_post = Post.objects.get(slug=slug)
    return render(request,'posts/post-detail.html',{
        "post":specific_post,
        "post_tag":specific_post.tag.all()
    })