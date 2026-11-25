from django.contrib import admin
from .models import Categorie, Article


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug')
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date_publication', 'publie')
    list_filter = ('publie', 'categorie', 'date_publication')
    search_fields = ('titre', 'contenu', 'auteur')
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_publication'