from django.urls import path
from . import views

urlpatterns = [
    path("",view=views.ReviewView.as_view()),
    path("thank_you",view=views.thank_you,name='thank-you')
]
