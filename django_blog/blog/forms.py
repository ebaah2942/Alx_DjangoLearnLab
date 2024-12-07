from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag



class TagWidget(forms.CheckboxSelectMultiple):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs.update({'class': 'form-control', 'style': 'width: 300px;'})

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
    # tags = forms.CharField(required=False, widget=forms.CheckboxSelectMultiple( 
    #     attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': ["TagWidget()"],

        }
       

        labels = {
            'title': 'Title',
            'content': 'Content',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            instance.save()
            if tags:
                tag_names = [t.strip() for t in tags.split(',')]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    instance.tags.add(tag)
        return instance



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
                        



