from django import forms
from .models import Commentaire, Article
from django.utils.text import slugify


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom', 'email', 'contenu']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Ton nom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ton@email.com'}),
            'contenu': forms.Textarea(attrs={'placeholder': 'Ton commentaire...', 'rows': 4}),
        }


from .models import Article  # adapte l'import existant en haut


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'auteur', 'categorie', 'publie']
        widgets = {
            'titre': forms.TextInput(attrs={'placeholder': "Titre de l'article"}),
            'contenu': forms.Textarea(attrs={'rows': 8, 'placeholder': "Contenu de l'article..."}),
            'auteur': forms.TextInput(attrs={'placeholder': 'Ton nom'}),
        }