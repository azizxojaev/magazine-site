from django.shortcuts import render
import datetime
from .utils import get_default_context
import math
from .models import *


def home_page(request):
    context = {}
    context = get_default_context(context)
    return render(request, 'index.html', context=context)

def category_page(request):
    news_obj = New.objects.all()
    tranding_news = news_obj.order_by('-views')[:5]

    if request.method == 'POST':
        tag = request.POST.get('tag')
        news_obj = news_obj.filter(tag__name=tag)

    news = [news_obj[i:i+13] for i in range(0, len(news_obj), 13)]
    context = {
        'news': news,
        'tranding_news': tranding_news
    }
    context = get_default_context(context)
    return render(request, 'category.html', context=context)

def contact_page(request):
    context = {}
    context = get_default_context(context)
    return render(request, 'contact.html', context=context)

def singe_page(request):
    context = {}
    context = get_default_context(context)
    return render(request, 'single.html', context=context)