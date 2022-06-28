from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=260)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"id": str(self.id)})