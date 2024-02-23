from django.shortcuts import render

from articles.models import Article


def articles_list(request):

    articles = Article.objects.all()
    articles = articles.order_by('-published_at')

    template = 'articles/news.html'
    context = {'object_list': articles}

    return render(request, template, context)
