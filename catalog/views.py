from django.shortcuts import render

from catalog.models import Author, Book, BookInstance

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances =  BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    books_avaiables = BookInstance.objects.filter(status__exact="a").count

    return render(
        request,
        "cat.html", 
        context={
            "num_books": num_books,
            "num_instances": num_instances,
            "num_authors": num_authors,
            "books_avaiables": books_avaiables,

        }
    )

