from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=260)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"pk": str(self.pk)})


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name="comments",
        on_delete=models.CASCADE
    )
    body = models.CharField(max_length=300)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.body[:50]

    def get_absolute_url(self):
        return reverse('articles')
