from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book

# Create your views here.

def createBook(request):
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
            book=Book(book_name=name,author=author,price=price,pages=pages,category=category)
            print("Saved")
            book.save()

            return redirect("list")

        else:
            form = BookForm(request.POST)
            context["form"] = form
            return render(request, "book/create_book.html", context)
    return render(request,"book/create_book.html",context)

def list_all_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book/listallBook.html",context)

def book_details(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/book_view.html",context)

def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("list")


def update_book(request,id):
    book=Book.objects.get(id=id)
    book_det={
        "name":book.book_name,
        "author":book.author,
        "price":book.price,
        "pages":book.pages,
        "category":book.category
    }
    form=BookForm(initial=book_det);
    context={}
    context["form"]=form
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            author = form.cleaned_data.get("author")
            price = form.cleaned_data.get("price")
            pages = form.cleaned_data.get("pages")
            category = form.cleaned_data.get("category")
            book.book_name=name
            book.author=author
            book.price=price
            book.pages=pages
            book.category=category
            book.save()
            return redirect("list")

    return render(request,"book/edit_book.html",context)

