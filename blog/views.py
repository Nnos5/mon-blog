from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.filter(publie=True)
    return render(request, 'blog/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)
    return render(request, 'blog/article_detail.html', {'article': article})