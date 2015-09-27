#Tutorial Database

This tutorial database is built on the idea that all complex tutorials can be subdivided into smaller sub-tutorials. In fact, any tutorial can be as simple as a single instruction with no sub-tutorials. It is reasonable to assume that these simple single-instruction tutorials could be useful across many different complex tutorials. By using this linked structure, and writing tutorials in a more general format, one can prevent having to re-write reusable instructions. Drafting a complex tutorial can then be as simple as linking to existing complex or single-instructions tutorials. Thus, as the collection of simple tutorials grows, so does the potential for more complex tutorials (both in increased complexity and numbers of individual tutorials).

This Django app requires the image processing library Pillow:
http://pillow.readthedocs.org/en/latest/installation.html
* Note: Sometimes it works with Pip, sometimes it works with easy_install. If not one, try the other

As well as the sortedm2m python Package:
https://pypi.python.org/pypi/django-sortedm2m
* Note: be sure to add 'sortedm2m' to tutsite/settings.py file INSTALLED_APPS = () list

