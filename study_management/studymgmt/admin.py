from django.contrib import admin
from .models import Study, StudyLog
# Register your models here.
@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ["study_id","study_name"]
    list_display_links = ["study_id","study_name"]
    list_filter = ["study_phase","sponser_name"]
    search_fields = ["study_name","sponser_name","study_id"]
    
admin.site.register(StudyLog)
