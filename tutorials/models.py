from django.db import models
from sortedm2m.fields import SortedManyToManyField
import time
from django.contrib.auth.models import User
import string


def content_file_name(instance, filename):
    doug = str(filename)
    pete = time.strftime("%Y%m%d_%H%M%S") + doug[doug.rfind('.'):]
    return '/'.join(['images', str(instance.user.id), pete])


class TutComment(models.Model):
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text

    def com_type(self):
        return 'text'


class TutImageComment(TutComment):
    photo = models.ImageField(upload_to=content_file_name, blank=True)  # uses the content_file_name function above
    user = models.ForeignKey(User, default='derek')  # to be set by the form from the current logged in user

    def com_type(self):
        return 'image'

class TutUrlComment(TutComment):
    link = models.URLField(max_length=2000, blank=True)

    def com_type(self):
        return 'url'


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    subtuts = SortedManyToManyField('self', blank=True, symmetrical=False)
    tut_comms = SortedManyToManyField(TutComment, blank=True, symmetrical=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title