from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    author=models.CharField(max_length=120)
    price=models.IntegerField()
    pages=models.IntegerField()
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

#>>>book1=Book(book_name="The Alchemist",author="Paulo Coelho",price=200,pages=160,category="Novel")
#>>>book1.save()
#>>> books=Book.objects.all()
#>>> books
#>>> book=Book.objects.get(id=1)
#print(book.book_name)
