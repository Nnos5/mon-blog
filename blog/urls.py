from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/nouveau/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]