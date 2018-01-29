#-*- coding:utf8 -*-
from django.shortcuts import render,redirect
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from website.form import LoginForm
from django.http import HttpResponse
#用于用户注册,以及登录
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def listing(request, cate=None):
    context = {}
    if cate is None:
        vids_list = models.Video.objects.all()
    elif cate == 'editors':
        vids_list = models.Video.objects.filter(editors_choice=False)
    # 分页可能会产生无序的结果
    page_robot = Paginator(vids_list, 9)
    page_num = request.GET.get('page')
    try:
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)
        # raise Http404('EmptyPage!')
    except PageNotAnInteger:
        vids_list = page_robot.page(1)

    context['vids_list'] = vids_list
    return render(request, 'listing.html', context)

def index_login(request):
    context = {}
    # 渲染表单
    #未用AuthenticationForm做登录
    # if request.method == 'GET':
    #     form = LoginForm
    # elif request.method == 'POST':
        #未用AuthenticationForm做登录

        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     # 看这个用户存不存在
        #     user = authenticate(username=username, password=password)
        #     if user:
        #         login(request, user)
        #         return redirect(to='list')
        #     else:
        #         return HttpResponse('<h1>NOT A USER!</h1>')

    #用AuthenticationForm做登录
    #其中不需要再把user,pass传入authenticate校验.因为AuthenticationForm在内部
    #已经做了检验了.
    if request.method == 'GET':
        form = AuthenticationForm
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #成立的话直接登录
            login(request, form.get_user())
            return redirect(to='list')

    context['form'] = form
    return render(request, 'register_login.html', context)

def index_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    elif request.method == 'POST':
        #注册的参数不需要指定data=
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #表单验证没有问题的话直接save(UserCreationForm会做用户名存不存在,密码是否一致等的验证.可查看源码)
            form.save()
            return redirect(to='login')

    context['form'] = form
    return render(request, 'register_login.html', context)
