from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def starting_page(request):
    return render(request,'posts/index.html')

def all_post(request):
    return render(request,'posts/all-posts.html')

def post_details(request,slug):
    pass