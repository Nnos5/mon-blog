from django.contrib import admin
from .models import Categorie, Article, Commentaire


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug')
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date_publication', 'publie')
    list_filter = ('publie', 'categorie', 'date_publication')
    search_fields = ('titre', 'contenu', 'auteur_username')
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_publication'
    fields = ('titre', 'slug', 'contenu', 'image', 'auteur', 'categorie', 'publie')
    
@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'article', 'date_creation', 'approuve')
    list_filter = ('approuve' , 'date_creation')
    search_filter = ('nom', 'email', 'contenu')