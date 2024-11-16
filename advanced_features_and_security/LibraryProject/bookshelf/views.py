from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def view_article(request, article_id):
    if not request.user.has_perm('app_name.can_view'):
        return HttpResponseForbidden("You do not have permission to view this article.")
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})
