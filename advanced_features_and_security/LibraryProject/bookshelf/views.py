from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib.auth.decorators import permission_required
from .forms import ArticleForm
from django.shortcuts import render, redirect
from .models import Book
@login_required
def view_article(request, article_id):
    if not request.user.has_perm('app_name.can_view'):
        return HttpResponseForbidden("You do not have permission to view this article.")
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})



@permission_required('app_name.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # Redirect to article list or success page
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')  # Redirect to article list after deletion
    return render(request, 'delete_article.html', {'article': article})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
