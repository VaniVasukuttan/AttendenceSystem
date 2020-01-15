from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login',TemplateView.as_view(template_name='login.html'),name='login'),
    path('assessment',TemplateView.as_view(template_name='assessment.html'),name='assessment'),
    path('attendence',TemplateView.as_view(template_name='attendence_1.html'),name='attendence'),
    path('dashboard',TemplateView.as_view(template_name='dashboard.html'),name='dashboard'),
    path('faculty-batch',TemplateView.as_view(template_name='faculity_home_batch.html'),name='fac-batch'),   
    path('faculty-login',TemplateView.as_view(template_name='faculty-login.html'),name='fac-login'), 
    path('faculty-profile-edit',TemplateView.as_view(template_name='faculty-profile-edit.html'),name='fac-profile-edit'),
    path('faculty-profile',TemplateView.as_view(template_name='faculty-profile.html'),name='fac-profile'),
    path('leave-forwarded',TemplateView.as_view(template_name='leave-forwarded.html'),name='leave-forward'),
    path('leave-rejected',TemplateView.as_view(template_name='leave-rejected.html'),name='leave-rejected'),
    path('student-leave',TemplateView.as_view(template_name='student-leave.html'),name='stud-leave'),
    #path('logins',views.login_request, name='login_req'),
   
]

