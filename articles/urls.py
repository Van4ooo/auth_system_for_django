from django.urls import path

from .views import ArticlePageView

urlpatterns = [
    path('', ArticlePageView.as_view(), name="articles"),
]