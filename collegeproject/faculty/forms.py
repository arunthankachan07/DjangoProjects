from django import forms

class FacultyRegistrationForm(forms.Form):
    firstname=forms.CharField(max_length=120)
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=100)


class FacultyLoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=100)
