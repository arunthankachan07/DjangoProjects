from django.forms import ModelForm
from .models import Product,Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'text_inp', 'placeholder': 'Price'}),
            'specs': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Specs'}),
            'image': forms.FileInput(attrs={'class': 'text_inp', 'placeholder': 'Image'}),

        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'UserName'}),
            'email': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'text_inp', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'text_inp', 'placeholder': 'Confirm Password'}),

        }
        # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        #     'class': 'text_inp', 'placeholder': 'Password'}))


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp',}),label='Username')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'text_inp',}),label='Password')

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["address","product","user"]
