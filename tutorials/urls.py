from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tut_list, name='tut_list'),
    url(r'^tutorials/(?P<tut_id>[0-9]+)/$', views.tut_detail, name='tut_detail'),
    url(r'^tutorial/new/$', views.tut_builder, name='tut_builder'),
]

'''
url(r'^tutorial/(?P<tut_id>[0-9]+)/$', views.tut_detail, name='tut_detail')
~ ^ means "the beginning"
~ tutorial/ only means that after the beginning, the URL should contain the word post and /
~ (?P<tut_id>[0-9]+) means that Django will take everything that you place here and transfer it to a view as a variable called tut_id
 ~ [0-9] means that it can only be a number, not a letter (so everything between 0 and 9)
 ~ + means that there needs to be one or more digits
  ~ So something like http://127.0.0.1:8000/tutorial// is not valid, but http://127.0.0.1:8000/tutorial/1234567890/ is ok
~ $ means the end of the url string
'''