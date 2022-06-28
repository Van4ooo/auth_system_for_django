from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article


class ArticlePageView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "article_list"


class ArticleDetailPageView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


class ArticleDeletePageView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    context_object_name = "article"

    success_url = reverse_lazy('articles')


class ArticleEditPageView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    context_object_name = "article"

    fields = ('title', 'body')


__all__ = [
    'ArticlePageView',
    'ArticleDetailPageView',
    'ArticleDeletePageView',
    'ArticleEditPageView'
]