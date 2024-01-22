from django.urls import path,include
from . import views


urlpatterns = [
    path('',view=views.starting_page,name='starting-page'),
    path('posts',view=views.all_post,name='posts-page'),
    path('posts/<slug:slug>',view=views.post_details,name='post-detail-page')
]
