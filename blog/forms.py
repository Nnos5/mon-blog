from django import forms
from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom', 'email', 'contenu']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Ton nom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ton@email.com'}),
            'contenu': forms.Textarea(attrs={'placeholder': 'Ton commentaire...', 'rows': 4}),
        }