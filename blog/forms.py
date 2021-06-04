from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class NameForm(forms.Form):
	login = forms.CharField(label='login', max_length=10)
	senha = forms.CharField(label='senha', max_length=10)	