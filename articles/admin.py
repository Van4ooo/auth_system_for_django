from django.contrib import admin

from .models import Article, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentAdmin
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
