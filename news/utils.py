import datetime
from .models import *
import requests


def get_default_context(context):
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    tags = Tag.objects.all()
    context['date'] = date
    context['tags'] = tags
    context['tranding_news'] = New.objects.all().order_by('-views')[:5]
    return context
