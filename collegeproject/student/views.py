from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm,LoginForm


# Create your views here.
def get_student_registration(request):
    context={}
    form=StudentRegistrationForm()
    context["form"]=form
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            studentname=form.cleaned_data.get("f_name")
            username=form.cleaned_data.get("u_name")
            password=form.cleaned_data.get("pwd")
            phone=form.cleaned_data.get("ph_no")
            course=form.cleaned_data.get("course")
            age=form.cleaned_data.get("age")
            print(studentname,username,password,phone,course,age)
            return redirect("signin")
        else:
            form=StudentRegistrationForm(request.POST)
            context["form"]=form
            return render(request,"student/studentreg.html",context)

    return render(request,"student/studentreg.html",context)

def get_login(request):
    context = {}
    form = LoginForm()
    context["form"] = form

    return render(request,"student/studentlogin.html",context)

def get_feedback(request):
    return render(request,"student/postfeedback.html")


def fetch_data(request):
    firstname=request.POST.get("f_name")
    uname=request.POST.get("u_name")
    password=request.POST.get("pwd")
    phone=request.POST.get("ph_no")
    course=request.POST.get("course")
    print(firstname,",",uname,",",password,",",phone,",",course)
    return render(request,"student/studentlogin.html")

def fetch_data_login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(username,",",password)
    return render(request,"student/student_home.html")
