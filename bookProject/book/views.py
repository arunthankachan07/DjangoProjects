from django.shortcuts import render,redirect
from .forms import BookForm

# Create your views here.

def get_book_info(request):
    context={}
    form=BookForm()
    context["form"]=form
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            author=form.cleaned_data.get("author")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            category=form.cleaned_data.get("category")
            print(name,author,price,pages,category)

        else:
            form = BookForm(request.POST)
            context["form"] = form
            return render(request, "book/create_book.html", context)
    return render(request,"book/create_book.html",context)