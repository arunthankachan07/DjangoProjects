from django import forms

class StudentRegistrationForm(forms.Form):
    f_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    u_name=forms.CharField(widget=forms.TextInput(attrs={'class':'txtin'}))
    pwd=forms.CharField(widget=forms.PasswordInput)
    ph_no=forms.CharField(max_length=15)
    course = forms.CharField(max_length=15)
    age=forms.CharField(max_length=10)

    def clean(self):
        cleaned_data=super().clean()
        age=cleaned_data.get("age")
        if int(age)<18:
            msg="invalid age"
            self.add_error("age",msg)


class LoginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(max_length=50)