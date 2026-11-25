from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article
from .forms import CommentaireForm

def article_list(request):
    query = request.GET.get('q', '').strip()
    articles = Article.objects.filter(publie=True)

    if query:
        articles = articles.filter(
            Q(titre__icontains=query) |
            Q(contenu__icontains=query) |
            Q(auteur__icontains=query)
        )

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/article_list.html', {
        'page_obj': page_obj,
        'query': query,          
    })
    query = request.GET.get('q', '').strip()
    articles = Article.objects.filter(publie=True)

    if query: 
        articles = articles.filter(
            Q(titre__contains=query) |
            Q(contenu__contains=query) |
            Q(auteur__contains=query)
        )

    paginator = Paginator(articles, 5)  # 5 articles par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html',
     {'page_obj': page_obj},
     {'query':query,
     })
     

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, publie=True)
    commentaires = article.commentaires.filter(approuve=True)
    form = CommentaireForm()

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.save()
            return redirect('blog:article_detail', slug=article.slug)

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'commentaires': commentaires,
        'form': form,
    })