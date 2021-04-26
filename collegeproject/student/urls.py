"""collegeproject URL Configuration

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
from django.urls import path
from .views import get_student_registration,get_login,get_feedback,fetch_data,fetch_data_login

urlpatterns = [
    path("studregister",get_student_registration),
    path("login",get_login,name="signin"),
    path("feedback",get_feedback),
    path("fetchdata",fetch_data,name="fetchdata"),
    path("loginpost",fetch_data_login,name="postsignin")

]
