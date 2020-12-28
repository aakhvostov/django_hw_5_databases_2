from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    ordering = '-published_at'
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related('scopes').order_by(ordering).all()
    for article in articles:
        for scope in article.scopes.all():
            article_set = scope.article_topic.get(article=article)
            scope.is_main = article_set.is_main
    context = {'object_list': articles}

    return render(request, template, context)
