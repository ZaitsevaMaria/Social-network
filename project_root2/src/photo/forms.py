from django import forms
from photo.models import Post, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'photo')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class SearchUserFormByUsername(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for',
    widget=forms.TextInput(attrs={'size': 32, 'class':'form-control search-query'}))