from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article


def article_list(request):
    articles = Article.objects.filter(publie=True)
    paginator = Paginator(articles, 5)  # 5 articles par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'page_obj': page_obj})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)
    return render(request, 'blog/article_detail.html', {'article': article})