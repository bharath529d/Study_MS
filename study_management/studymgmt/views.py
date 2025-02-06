from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import StudyForm
import logging
from django.forms import model_to_dict
from .shared_data import field_names
from datetime import datetime
from .tasks import log_event
from .models import StudyLog, Study

logger = logging.getLogger('operations')

# Create your views here.
def main(request):
    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('selected_objects_ids')
        log_event.after_response(request.method,"Delete Study",f"Deleted Studies [id={ids_to_delete}]",datetime.now().replace(microsecond=0))
        logger.info(f"Deleting selected studies-{ids_to_delete}")
        Study.objects.filter(study_id__in=ids_to_delete).delete()
    studies = Study.objects.all().order_by('-study_id') # getting all the objects from the model
    if studies:
        log_event.after_response(request.method,"Retrieve Studies","Retrieved all the studies",datetime.now().replace(microsecond=0))
        return render(request,'studymgmt/main.html',{'studies':studies})
    else:
        log_event.after_response(request.method,"Retrieve Studies","Retrieved Studies & No Study at present",datetime.now().replace(microsecond=0))
        return render(request,'studymgmt/main.html',{'empty':True})

def add_study(request):
    if request.method == 'POST':
        studyform = StudyForm(request.POST)
        print(request.POST)
        if studyform.is_valid():   # if data is valid, further steps are taken

            Study.objects.create(**studyform.cleaned_data) # adding studying
            given_study_id = Study.objects.values('study_id').order_by('-study_id').first()['study_id']
            log_event.after_response(request.method,"Add Study",f"New Study added [id={given_study_id}]",datetime.now().replace(microsecond=0))
            logger.info(f"New Study Added views {datetime.now()}")
            return redirect('main')
    else:       # when request_method is GET
        studyform = StudyForm()
        sponser_names = Study.objects.values('sponser_name').distinct()  # getting unique sponser_names 
        studyform.fields['sponser_name'].widget.datalist = sponser_names  # setting the sponser_names to the datalist in the rendered widget
    return render(request,'forms/addstudy.html',{'form':studyform}) # executed if  it is GET or if data is invalid
                                                                   


def not_found(request):
    return render(request,'404.html')

def study_info(request, id):
    try:
        # retrieve the values of all the fields of a single object as a list
        studydata = Study.objects.filter(study_id=id).values_list().first()
        study_name= studydata[1]  # getting the study_name value since 0th index is study_id
        log_event.after_response(request.method,"View Study",f"Viewed Study [id={id}]",datetime.now().replace(microsecond=0))
        logger.info(f"Viewing Study whose id is {id}") # logging
         #combining fields names and its corresponding values
        studydata = zip(field_names,studydata[1:]) # zipped together the field_names and field_values
        return render(request,'studymgmt/studyinfo.html',{'studydata':studydata,'study_name':study_name})
    except:
        log_event.after_response(request.method,"View Study",f"Requested Study whose id is {id} Not Found",datetime.now().replace(microsecond=0))
        return redirect('not_found') # if study doesn't exit
   

def update_study(request, id):
    try:
        studydata = Study.objects.get(study_id=id)
    except:
        return redirect('not_found')          # if study doesn't exit
    studydata_dict = model_to_dict(studydata)   # converting model to dict for ease of access
    if request.method == 'POST':
        studyform = StudyForm(request.POST,initial=studydata_dict)
        if studyform.has_changed():
            if studyform.is_valid():
                logger.info(f"Update Study whose id is {id}")
                log_event.after_response(request.method,"Update Study",f"Updated Study [id ={id}], changed fields = {studyform.changed_data}",datetime.now().replace(microsecond=0))
                for field_name in studyform.changed_data:
                        setattr(studydata,field_name,studyform.cleaned_data[field_name]) # setting the new data to the corresponding fields
                studydata.save()
                print()
                return redirect('main')
            else: # if submitted_data is invalid
                    log_event.after_response(request.method,"Update Study",f"Provided Invalid data while updating [id={id}]",datetime.now().replace(microsecond=0))
                    return render(request,'forms/update_study.html',{'form':studyform})
        else:  # if no changes has done
            return render(request,'forms/update_study.html',{'form':studyform})
    else:
        studyform = StudyForm(initial=studydata_dict) 
    return render(request,'forms/update_study.html',{'form':studyform}) # executed if GET or
                                                                         # if the data is invalid
