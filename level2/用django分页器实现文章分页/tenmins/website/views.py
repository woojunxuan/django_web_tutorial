from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
