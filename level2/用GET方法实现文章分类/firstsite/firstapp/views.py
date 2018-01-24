from django.shortcuts import render
from firstapp.models import People, Aritcle, Comment


def index(request):
    context = {}
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Aritcle.objects.filter(tag=queryset)
    else:
        article_list = Aritcle.objects.all()
    context['article_list'] = article_list
    # render函数,简便快捷的渲染一个网页
    web_page = render(request, 'firstweb.html', context)
    return web_page
