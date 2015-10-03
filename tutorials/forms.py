from django import forms
from .models import Tutorial, TutComment

class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        #fields = ('title', 'text', 'subtuts', 'tut_comms')
        fields = ('title', 'text','subtuts', 'tut_comms',)