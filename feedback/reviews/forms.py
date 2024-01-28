from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100,label="Your Name",error_messages={
        "required":"It is a required field!.you can not leave it empty.",
        "max_length":"Max length can not be more than 100"
    })  

    review_text = forms.CharField(label="Review Text",widget=forms.Textarea,max_length=200)
    rating = forms.IntegerField(label='Rating',min_value=1,max_value=5)