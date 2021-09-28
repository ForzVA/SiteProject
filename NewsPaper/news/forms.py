from django.forms import ModelForm, BooleanField, TextInput, Textarea
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Confirm')

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'categorySelection', 'check_box']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
                   'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the text'}),

                   }


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
