from django.urls import path

from .views import ArticlePageView, ArticleDetailPageView

urlpatterns = [
    path('', ArticlePageView.as_view(), name="articles"),
    path('<int:pk>/', ArticleDetailPageView.as_view(), name="article_detail")
]