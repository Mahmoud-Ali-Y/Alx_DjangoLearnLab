from django import forms
from .models import Post, Comment
from taggit.managers import TaggableManager
 
# create a ModelForm
class PostForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Post
        fields = "__all__"
        tags = TaggableManager()
class CommentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Comment
        fields = "content"