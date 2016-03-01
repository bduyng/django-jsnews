from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-created_time')
    paginator = Paginator(latest_article_list, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    # convert created_time
    for article in articles.object_list:
        article.created_time = article.created_time.strftime("%Y-%m-%dT%H:%M:%S")
    return render(request, 'articles/index.html', {
        'articles': articles,
        'paginator': paginator
    })
