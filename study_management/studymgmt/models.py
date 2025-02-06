from django.db import models

# Create your models here.
class Study(models.Model):
    PHASES = [
        ('PHASE-I','PHASE-I'),
        ('PHASE-II','PHASE-II'),
        ('PHASE-III','PHASE-III'),
        ('PHASE-IV','PHASE-IV'),
    ]
    study_id = models.AutoField(primary_key=True)
    study_name = models.CharField(max_length=100)
    study_phase = models.CharField(max_length=10,choices=PHASES)
    sponser_name = models.CharField(max_length=100)
    study_descrip = models.TextField()

    def __str__(self):
        return "-".join([self.study_name,"id",str(self.study_id)])

class StudyLog(models.Model):
    REQUEST_METHODS =[
        ('GET','GET'),
        ('POST','POST')
    ] 
    log_id = models.AutoField(primary_key=True)
    request_method = models.CharField(max_length=4, choices=REQUEST_METHODS)
    event = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "-".join([self.event,"id",str(self.log_id)])
