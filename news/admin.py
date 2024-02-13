from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget


admin.site.register(Tag)
admin.site.register(NewsView)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(ReplyComment)
admin.site.register(Contact)

class NewModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(New, NewModelAdmin)