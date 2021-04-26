from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=150)
    desig=models.CharField(max_length=100)
    salary=models.IntegerField()

    def __str__(self):
        return self.name



#----------------------------------
# >>> from employee.models import Employee

#CREATE 4 EMPLOYEE OBJECTS

# >>> emp=Employee(name="Ajmal",desig="QA",salary=25000)
# >>> emp.save()
# >>> emp=Employee(name="Ram",desig="Developer",salary=27000)
# >>> emp.save()
# >>> emp=Employee(name="Joy",desig="Testing",salary=23000)
# >>> emp.save()
# >>> emp=Employee(name="Sanju",desig="Developer",salary=27000)
# >>> emp.save()

#FETCH ALL EMPLOYEE OBJECTS

# >>> emp_det=Employee.objects.all()
# >>> emp_det
# <QuerySet [<Employee: Ajmal>, <Employee: Ram>, <Employee: Joy>, <Employee: Sanju>]>

#PRINT THEIR NAME

# >>> emp_det=Employee.objects.all()
# >>> for emp in emp_det:
# ...     print(emp.name)
# ...
# Ajmal
# Ram
# Joy
# Sanju

#FETCH A PARTICULAR EMPLOYEE

# >>> emp=Employee.objects.get(id=2)
# >>> emp
# <Employee: Ram>

#UPDATE A EMPLOYEE SALARY WHOSE ID = 3

# >>> emp=Employee.objects.get(id=3)
# >>> emp.salary=30000
# >>> emp.salary
# 30000
# >>>
