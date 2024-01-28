from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100,label="Your Name",error_messages={
#         "required":"It is a required field!.you can not leave it empty.",
#         "max_length":"Max length can not be more than 100"
#     })  

#     review_text = forms.CharField(label="Review Text",widget=forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label='Rating',min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = "__all__"
        # exclude = ['owner_comment']
        labels = {
            "user_name":"Your Name",
            "review_text":"Review Text",
            "rating":"Rating"
        }
        error_messages = {
            "user_name":{
                "required":"It is a required field!.you can not leave it empty.",
                "max_length":"Max length can not be more than 100"
            }
        }