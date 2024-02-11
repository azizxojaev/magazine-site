from django.shortcuts import render
import datetime
from .utils import get_default_context


def home_page(request):
    context = {}
    context = get_default_context(context)
    return render(request, 'index.html', context=context)

def category_page(request):
    context = {}
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