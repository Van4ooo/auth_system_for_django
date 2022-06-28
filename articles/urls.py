from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticlePageView.as_view(), name="articles"),
    path('<int:pk>/', ArticleDetailPageView.as_view(), name="article_detail"),
    path('<int:pk>/delete', ArticleDeletePageView.as_view(), name="article_delete")
]