from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from django.views import View
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

def thank_you(request):
    return render(request,'reviews/thank_you.html')