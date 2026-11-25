from django import forms
from .models import Commentaire, Article
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#--------formulation pour la creation d'un commentaire---_#

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

#---------creation d'un article --------__#

class ArticleForm(forms.ModelForm):
    nouvelle_categorie = forms.CharField(
        required=False,
        label="Ou créer une nouvelle catégorie",
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Tech, Voyage...'})
    )

    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image', 'categorie', 'publie']
        widgets = {
            'titre': forms.TextInput(attrs={'placeholder': "Titre de l'article"}),
            'contenu': forms.Textarea(attrs={'rows': 8, 'placeholder': "Contenu de l'article..."}),
        }


#------formulaire de creation de compte user-----_#

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'ton.email@exemple.com'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}),
        }