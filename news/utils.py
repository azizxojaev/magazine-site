import datetime


def get_default_context(context):
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    context['date'] = date
    return context
