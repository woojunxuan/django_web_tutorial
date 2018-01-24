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

# def detail(request, page_num):
#     context = {}
#     if request.method == "GET":
#         # 如果是get,则进行表单的创建,这个时候是未绑定表单
#         form = CommentForm
#     elif request.method == "POST":
#         # 绑定表单,只有当表单绑定的时候才能进行数据检验
#         form = CommentForm(request.POST)
#         # 校验表单数据,符合规则返回True,否则False
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             article = Aritcle.objects.get(id=page_num)
#             c = Comment(name=name, comment=comment, belong_to=article)
#             c.save()
#             return redirect(to='detail', page_num=page_num)
#     article = Aritcle.objects.get(id=page_num)
#     print(article.id)
#     context['article'] = article
#     context['form'] = form
#     return render(request, 'article_detail.html', context)

def detail(request, page_num, error_form=None):
    context = {}
    form = CommentForm
    article = Aritcle.objects.get(id=page_num)
    context['article'] = article
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'article_detail.html', context)


def detail_comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        article = Aritcle.objects.get(id=page_num)
        c = Comment(name=name, comment=comment, belong_to=article)
        c.save()
        return redirect(to='detail', page_num=page_num)
    else:
        return detail(request, page_num, error_form=form)
