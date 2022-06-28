from django.views.generic import ListView

from .models import Article


class ArticlePageView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "article_list"
