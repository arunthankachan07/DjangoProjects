from django import forms

class EmployeeForm(forms.Form):
    emp_name=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Employee Name'}),label='')
    desig=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Designation'}),label='')
    salary=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Salary'}),label='')
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Location'}),label='')
