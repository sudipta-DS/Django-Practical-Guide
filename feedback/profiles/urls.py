from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProfilesCreateView.as_view()),
    path("all-profiles",view=views.ProfileListView.as_view())
]
