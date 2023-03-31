from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'message', 'company', 'recipients', 'visit_date', 'post_date', 'stars', 'upload' )
