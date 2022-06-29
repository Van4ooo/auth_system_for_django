from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Article, Comment


class ArticlePageView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "article_list"


class ArticleDetailPageView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


class ArticleDeletePageView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    context_object_name = "article"

    login_url = 'login'
    success_url = reverse_lazy('articles')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleEditPageView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_edit.html"
    context_object_name = "article"

    login_url = 'login'

    fields = ('title', 'body')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreatePageView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ('title', 'body')

    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class CommentDetailPageView(DetailView):
    model = Comment
    template_name = "comment_detail.html"
    context_object_name = "comment"


__all__ = [
    'ArticlePageView',
    'ArticleDetailPageView',
    'ArticleDeletePageView',
    'ArticleEditPageView',
    'ArticleCreatePageView',
    'CommentDetailPageView'
]
