"""employeeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import createEmployee,employee_list,employee_view,employee_delete,employee_update

urlpatterns = [
    path("create",createEmployee,name="createemployee"),
    path("list",employee_list,name="emp_list"),
    path("view/<int:id>", employee_view, name="emp_view"),
    path("delete/<int:id>", employee_delete, name="emp_delete"),
    path("edit/<int:id>", employee_update, name="emp_update")

]
