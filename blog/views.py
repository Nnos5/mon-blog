from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Categorie, Commentaire
from .forms import CommentaireForm, ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.utils.text import slugify
from django.views.generic import CreateView
from .forms import SignUpForm


def article_list(request):
    query = request.GET.get('q', '').strip()
    articles = Article.objects.filter(publie=True)

    if query:
        articles = articles.filter(
            Q(titre__icontains=query) |
            Q(contenu__icontains=query) |
            Q(auteur__username__icontains=query)
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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')

    def form_valid(self, form):
        # 1. L'auteur = l'utilisateur connecté  ← AVANT tout le reste
        form.instance.auteur = self.request.user

        # 2. Créer la catégorie si demandée
        nouvelle_cat = form.cleaned_data.get('nouvelle_categorie', '').strip()
        if nouvelle_cat:
            base_slug = slugify(nouvelle_cat)
            slug = base_slug
            counter = 1
            while Categorie.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            categorie, _ = Categorie.objects.get_or_create(
                nom=nouvelle_cat,
                defaults={'slug': slug}
            )
            form.instance.categorie = categorie

        # 3. Slug unique de l'article
        base_slug = slugify(form.cleaned_data['titre'])
        slug = base_slug
        counter = 1
        while Article.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        form.instance.slug = slug

        return super().form_valid(form)
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')

    


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_queryset(self):
        # 👈 Seul l'auteur peut modifier son article
        return Article.objects.filter(auteur=self.request.user)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:article_list')
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_queryset(self):
        # 👈 Seul l'auteur peut supprimer son article
        return Article.objects.filter(auteur=self.request.user)


class MyArticlesView(LoginRequiredMixin, ListView):
    template_name = 'blog/my_articles.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(auteur=self.request.user).order_by('-date_publication')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles_qs = Article.objects.filter(auteur=self.request.user)
        context['total_articles'] = articles_qs.count()
        context['total_publies'] = articles_qs.filter(publie=True).count()
        context['total_brouillons'] = articles_qs.filter(publie=False).count()
        context['total_commentaires'] = Commentaire.objects.filter(article__auteur=self.request.user).count()
        return context

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def custom_404(request, exception):
    return render(request, '404.html', status=404)