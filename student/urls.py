from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('home',TemplateView.as_view(template_name='home.html'),name='home'),
    path('student-profile',TemplateView.as_view(template_name='student-profile.html'),name='stud-profile'),
    path('student-login',TemplateView.as_view(template_name='studlogins.html'),name='stud-login'),
    path('student-attendence',TemplateView.as_view(template_name='student-attendence.html'),name='stud-attendence'),
    path('student-edit',TemplateView.as_view(template_name='student-edit.html'),name='stud-login'),
    path('student-leave',TemplateView.as_view(template_name='student-leave-management.html'),name='stud-leave'),
    path('student-applied-leave',TemplateView.as_view(template_name='student-applied-leave.html'),name='stud-leaveapplied'),
    path('header',TemplateView.as_view(template_name='header.html'),name='header'),
    path('student-assessment',TemplateView.as_view(template_name='student-assessment.html'),name='studassess'),

]