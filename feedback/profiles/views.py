from msilib.schema import ListView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import ProfileForm
from .models import ProfilesModel
# Create your views here.

class ProfilesCreateView(CreateView):
    model = ProfilesModel
    fields = '__all__'
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"

class ProfileListView(ListView):
    template_name = 'profiles/user-profiles.html'
    model = ProfilesModel
    context_object_name = 'profiles'

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form" : form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid():
#             profile_image = ProfilesModel(image=request.FILES['user_image'])
#             profile_image.save()
#             # print(img)
#             return render(request, "profiles/create_profile.html",{
#                 "form" : submitted_form
#             })
