from django.shortcuts import render
from faculty.models import faculties
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from student import urls

def login_request(request):
     if request.method=='POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        email=str(email)
        password=str(password)
        u=faculties.objects.filter(f_password=password)
        p=faculties.objects.filter(f_email=email)
        if u.count()==1 and p.count()==1:
            return render(request,'faculty-login.html')
        else:
            if (email=='student' and password=='student'):
                return render(request,'home.html')

