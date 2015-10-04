from django.shortcuts import render, get_object_or_404
from .models import Tutorial, TutComment, TutImageComment, TutUrlComment
from .forms import TutorialForm
from django.shortcuts import redirect
from django.db.models import Count


def tut_list(request):
    tuts = Tutorial.objects.all().annotate(num_subs=Count('subtuts')).order_by('-num_subs')
    return render(request, 'tutorials/tut_list.html', {'all_tuts': tuts})

def tut_detail(request, tut_id):
    tut = get_object_or_404(Tutorial, id=tut_id) #get the specific tutorial object
    subs = Tutorial.objects.get(id=tut_id).subtuts.all()
    qset = Tutorial.objects.get(id=tut_id).tut_comms.all()
    tcoms = []
    for ob in qset:
        if hasattr(ob, 'tutimagecomment'):
            tcoms.append(TutImageComment.objects.get(id=ob.id))
        elif hasattr(ob, 'tuturlcomment'):
            tcoms.append(TutUrlComment.objects.get(id=ob.id))
        else:
            tcoms.append(ob)
    return render(request, 'tutorials/tut_detail.html', {'tut': tut, 'subs':subs, 'tcoms': tcoms})

def tut_builder(request):
    if request.method == "POST": #for when the form has been filled out and the save button clicked
        form = TutorialForm(request.POST)
        if form.is_valid():
            tut = form.save(commit=False)
            tut.save()
            return redirect('tutorials.views.tut_detail', tut_id = tut.pk)
    else: #for empty form
        form = TutorialForm()
    return render(request, 'tutorials/tut_builder.html', {'form': form})
