from django.contrib import admin
from .models import Tutorial, TutImageComment, TutComment, TutUrlComment

admin.site.register(Tutorial)
admin.site.register(TutImageComment)
admin.site.register(TutComment)
admin.site.register(TutUrlComment)