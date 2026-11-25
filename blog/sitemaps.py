from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Article.objects.filter(publie=True)

    def lastmod(self, obj):
        return obj.date_publication

    def location(self, obj):
        return reverse('blog:article_detail', kwargs={'slug': obj.slug})