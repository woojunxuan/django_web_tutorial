"""tenmins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#-*- conding:utf-8 -*-
from django.contrib import admin
from django.urls import path
from website.views import listing, index_login, index_register
from django.conf import settings
from django.conf.urls.static import static
#借用django自带的logout
from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', listing, name="list"),
    path('list/<cate>/', listing, name="list"),
    path('login/', index_login, name="login"),
    path('register/', index_register, name="register"),
    # logout后,跳转到login页面
    path('logout/', logout, {'next_page': 'register'}, name="logout"),
]

# 如果是开发模式
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
