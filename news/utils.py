import datetime
from .models import *
import requests


def get_default_context(context):
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    tags = Tag.objects.all()
    context['date'] = date
    context['tags'] = tags
    return context
