from django.contrib import admin
from .models import Tutorial, TutImageComment, TutComment

admin.site.register(Tutorial)
admin.site.register(TutImageComment)
admin.site.register(TutComment)