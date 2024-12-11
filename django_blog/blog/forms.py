from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment



# class TagWidget(forms.CheckboxSelectMultiple):
#     def __init__(self, attrs=None):
#         super().__init__(attrs)
#         self.attrs.update({'class': 'form-control', 'style': 'width: 300px;'})

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        kwargs.pop('user', None)  # Retrieve the user instance
        allowed_fields = kwargs.pop('allowed_fields', None)
        super().__init__(*args, **kwargs)
     

        
        if allowed_fields != '__all__':
            # Restrict to allowed fields
            for field_name in list(self.fields.keys()):
                if field_name not in allowed_fields:
                    self.fields.pop(field_name) 


        # if user and not user.is_superuser:
        #     # Restrict fields for non-superusers
        #     restricted_fields = ['first_name', 'last_name', 'email', 'username', 'password']
        #     for field in self.fields.keys():
        #         if field not in restricted_fields:
        #             self.fields.pop(field)   


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 50%; height: 300px;', 'placeholder': 'Write your post here...'}),

            

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
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 300px; height: 100px;', 'placeholder': 'Write your comment here...'}),
        }

        labels = {
            'content': 'Content',
        }

        def validate(self):
            super(CommentForm, self).validate()
            content = self.cleaned_data.get('content')
            if not content:
                self.add_error('content', 'Content is required')
                        



