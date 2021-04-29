from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employees

# Create your views here.
def createEmployee(request):
    context={}
    form=EmployeeForm()
    context["form"]=form
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            emp_name=form.cleaned_data.get("emp_name")
            desig=form.cleaned_data.get("desig")
            salary=form.cleaned_data.get("salary")
            location=form.cleaned_data.get("location")
            employee = Employees(emp_name=emp_name, desig=desig, salary=salary, location=location)
            print("Saved")
            employee.save()
            return redirect("emp_list")
    return render(request, "employee/Create_Employee.html",context)

def employee_list(request):
    employees=Employees.objects.all()
    context={}
    context["employees"]=employees
    return render(request,"employee/Employee_List.html",context)

def employee_view(request,id):
    employee=Employees.objects.get(id=id)
    context={}
    context["employee"]=employee
    return render(request,"employee/Employee_View.html",context)

def employee_delete(request,id):
    employee=Employees.objects.get(id=id)
    employee.delete()
    return redirect("emp_list")

def employee_update(request,id):
    employee=Employees.objects.get(id=id)
    emp={
        "emp_name":employee.emp_name,
        "desig":employee.desig,
        "salary":employee.salary,
        "location":employee.location
    }
    form=EmployeeForm(initial=emp);
    context={}
    context["form"]=form
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data.get("emp_name")
            desig = form.cleaned_data.get("desig")
            salary = form.cleaned_data.get("salary")
            location = form.cleaned_data.get("location")
            employee.emp_name=emp_name
            employee.desig=desig
            employee.salary=salary
            employee.location=location
            employee.save()
            return redirect("emp_list")

    return render(request,"employee/Employee_Edit.html",context)
