from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/nouveau/', views.ArticleCreateView.as_view(), name='article_create'),
    path('mes-articles/', views.MyArticlesView.as_view(), name='my_articles'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('article/<slug:slug>/modifier/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<slug:slug>/supprimer/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]