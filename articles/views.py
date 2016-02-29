from django.http import Http404
from django.shortcuts import render
from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-created_time')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'articles/index.html', context)
