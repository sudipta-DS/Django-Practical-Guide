from django.urls import path
from . import views

urlpatterns = [
    path("",view=views.ReviewView.as_view()),
    path("thank_you",view=views.ThankYouView.as_view(),name='thank-you'),
    path("reviews",view=views.ReviewListView.as_view()),
    path("reviews/<int:id>",view=views.SingleReviewView.as_view())
]
