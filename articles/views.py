from django.views.generic import ListView, DetailView, DeleteView, UpdateView

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


class ArticleEditPageView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    context_object_name = "article"


__all__ = [
    'ArticlePageView',
    'ArticleDetailPageView',
    'ArticleDeletePageView',
    'ArticleEditPageView'
]