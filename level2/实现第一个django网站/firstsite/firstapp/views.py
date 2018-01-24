from django.shortcuts import render
from firstapp.models import People, Aritcle


def index(request):
    context = {}
    article_list = Aritcle.objects.all()
    context['article_list'] = article_list
    # render函数,简便快捷的渲染一个网页
    web_page = render(request, 'firstweb.html', context)
    return web_page
