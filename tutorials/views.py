from django.shortcuts import render, get_object_or_404
from .models import Tutorial

def tut_list(request):
    tuts = Tutorial.objects.all()
    return render(request, 'tutorials/tut_list.html', {'all_tuts': tuts})

def tut_detail(request, tut_id):
    tut = get_object_or_404(Tutorial, id=tut_id) #get the specific tutorial object
    subs = Tutorial.objects.get(id=tut_id).subtuts.all()
    return render(request, 'tutorials/tut_detail.html', {'tut': tut, 'subs':subs})
