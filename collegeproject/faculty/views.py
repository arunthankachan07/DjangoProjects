from django.shortcuts import render
from .forms import FacultyRegistrationForm,FacultyLoginForm

# Create your views here.
def get_faculty_registration(request):
    context={}
    form=FacultyRegistrationForm()
    context["form"]=form
    return render(request,"faculty/facultyreg.html",context)

def get_fac_login(request):
    context={}
    form=FacultyLoginForm()
    context["form"]=form
    return render(request,"faculty/facultylog.html",context)

def fetchfacdata(request):
    firstname=request.POST.get("f_name")
    username=request.POST.get("u_name")
    password=request.POST.get("pwd")
    print(firstname,",",username,",",password)
    return render(request, "faculty/facultylog.html")

def fetchfaclogin(request):
    user=request.POST.get("uname")
    passwd=request.POST.get("pwd")
    print(user,",",passwd)
    return render(request,"faculty/facultyhome.html")