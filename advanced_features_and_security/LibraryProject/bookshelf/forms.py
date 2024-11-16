from django import forms
from .models import Article
from .models import ExampleModel 

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author'] 


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel  # Replace with your actual model
        fields = '__all__'
