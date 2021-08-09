from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Confirm')
    class Meta:
        model = Post
        fields = ['title', 'author', 'text', 'check_box']
