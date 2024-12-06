from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'     


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'content': 'Content',
        }

        def validate(self):
            super(CommentForm, self).validate()
            content = self.cleaned_data.get('content')
            if not content:
                self.add_error('content', 'Content is required')
                        



