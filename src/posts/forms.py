from django import  forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        # title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        # body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
