#name, author,price,pages,category
from django import forms

class BookForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Book Name'}),label='')
    author=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Author Name'}),label='')
    price=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Book Price'}),label='')
    pages=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Number of Pages'}),label='')
    category=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Category'}),label='')

    def clean(self):
        cleaned_data=super().clean()
        pages=cleaned_data.get("pages")
        if int(pages)<10:
            msg="Pages must be greater than 10"
            self.add_error("pages",msg)