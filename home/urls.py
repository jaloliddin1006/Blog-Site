from django.urls import path
from django.views.generic import ListView, DetailView
from .views import HomePageView, ArticleDetailView
from .models import Articles, Cantact
urlpatterns = [
  
    path('', HomePageView, name='home'),
 
    path('news/<int:pk>/', ArticleDetailView, name='article_detail'),
    # path('news/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
