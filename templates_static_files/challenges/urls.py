from django.urls import path
from . import views
urlpatterns = [
    path("",views.challenges,name='all-challenges'),
    path("<str:month>/",views.monthly_challenge,name='month-challenge'),
    path("<int:month>",views.monthly_challenges_by_number)
]