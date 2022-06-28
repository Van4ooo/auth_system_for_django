from django.views.generic import ListView, DetailView, DeleteView

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


__all__ = [
    ArticlePageView,
    ArticleDetailPageView,
    ArticleDeletePageView
]