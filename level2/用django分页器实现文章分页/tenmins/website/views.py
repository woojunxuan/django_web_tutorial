from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.
def listing(request):
    context = {}
    vids_list = models.Video.objects.all()
    print(vids_list.count())
    page_robot = Paginator(vids_list, 9)
    vids_list = page_robot.page(request.GET.get('page'))
    context['vids_list'] = vids_list
    return render(request, 'listing.html', context)
