from django.contrib import admin
from .models import *


admin.site.register(Tag)
admin.site.register(New)
admin.site.register(NewsView)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(ReplyComment)