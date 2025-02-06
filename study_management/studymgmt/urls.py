from django.urls import path
from .import views

urlpatterns = [
    path('addstudy/',views.add_study,name="addstudy"),
    path('study/<int:id>/',views.study_info,name="studyinfo"),
    path('update_study/<int:id>/',views.update_study,name="update_study"),
]