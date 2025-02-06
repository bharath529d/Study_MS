from django import forms
from .models import Study

def validate_study_descrip(value):
    if len(value) > 1024:
        raise forms.ValidationError("Maximum character length exceed (maxlength is 1024 characters)")

class InputList(forms.widgets.TextInput):
    template_name = "studymgmt/input_list_widget.html"
    def __init__(self,datalist_id,datalist,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.datalist_id = datalist_id
        self.datalist = datalist
        self.attrs['list'] = datalist_id
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['datalist_id'] = self.datalist_id
        context['widget']['datalist'] = self.datalist
        return context

def min_len_study_name(name):
    if len(name) < 3:
        raise forms.ValidationError("Study Name must be of atleast 3 character")
    
class StudyForm(forms.Form):
    PHASES = [
        ('PHASE-I',)*2,
        ('PHASE-II',)*2,
        ('PHASE-III',)*2,
        ('PHASE-IV',)*2,
    ]
    study_name = forms.CharField(validators=[min_len_study_name],label="STUDY NAME", error_messages={'required':'Study_name must not be left empty.'})
    study_phase = forms.ChoiceField(choices=PHASES, label="STUDY PHASE")
    sponser_name = forms.CharField(widget=InputList(datalist_id='sponsers',datalist=[]),label="SPONSER NAME")
    study_descrip = forms.CharField(widget=forms.Textarea(attrs={'rows':'15','cols':'30'}),label="STUDY DESCRIPTION",validators=[validate_study_descrip])
        
    

