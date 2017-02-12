from django import forms
from .models import Tweet


class TweetListForm(forms.Form):
    screen_name = forms.CharField(label="@ID")


class MyTweetListForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']
        widgets = {
            'text': forms.TextInput()
        }

