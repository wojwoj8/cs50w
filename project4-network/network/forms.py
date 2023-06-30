from django import forms

class PostForm(forms.Form):
    post = forms.CharField(required=True, label='Add Post', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add post here', 'id':'floatingTextarea'}))