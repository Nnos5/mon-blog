from django.db import models
from django.utils import timezone


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
    auteur = models.CharField(max_length=100)
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