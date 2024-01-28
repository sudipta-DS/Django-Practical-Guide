from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
# Create your views here.

class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,'reviews/review.html',{
        "form":form
        })

    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thank-you'))
        
        return render(request,'reviews/review.html',{
        "form":form
        })


# def index(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # form_data = Review(user_name=form.cleaned_data['user_name'],
#             #                    review_text=form.cleaned_data['review_text'],
#             #                    rating=form.cleaned_data['rating'])
#             form.save()
#             return HttpResponseRedirect(reverse('thank-you'))
#     else:
#         form = ReviewForm()
#     return render(request,'reviews/review.html',{
#         "form":form
#     })
    
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This Works!'
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     query_set = super().get_queryset()
    #     selected_query = query_set.filter(rating__gt=4)
    #     return selected_query
    
class SingleReviewView(TemplateView):
    template_name = "reviews/single-review.html"
    def get_context_data(self, **kwargs):
        review_id = kwargs['id']
        review = Review.objects.get(id=review_id)
        context = super().get_context_data(**kwargs)
        context["review"] = review
        # print(context)
        return context
    


# def thank_you(request):
#     return render(request,'reviews/thank_you.html')