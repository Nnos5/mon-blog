from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['nom']
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contenu = models.TextField()
    image = models.ImageField(            
        upload_to='articles/',
        blank=True,
        null=True
    )
    auteur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    date_publication = models.DateTimeField(default=timezone.now)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles'
    )
    publie = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_publication']  # plus récents d'abord
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='commentaires'
    )
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    approuve = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "commentaire"
        verbose_name_plural = "commentaires"

    def __str__(self):
        return f"Commentaire de {self.nom} sur « {self.article.titre} »"