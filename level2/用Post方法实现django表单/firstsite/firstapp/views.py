from django.shortcuts import render, redirect
from firstapp.models import People, Aritcle, Comment
from firstapp.forms import CommentForm


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

def detail(request):
    context = {}
    if request.method == "GET":
        # 如果是get,则进行表单的创建,这个时候是未绑定表单
        form = CommentForm
    elif request.method == "POST":
        # 绑定表单,只有当表单绑定的时候才能进行数据检验
        form = CommentForm(request.POST)
        # 校验表单数据,符合规则返回True,否则False
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            c = Comment(name=name, comment=comment)
            c.save()
            return redirect(to='detail')

    comment_list = Comment.objects.all()
    context['form'] = form
    context['comment_list'] = comment_list
    return render(request, 'article_detail.html', context)
