from django.shortcuts import redirect, render
from library.models import Author, Book, BookInstance

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username= request.user

        books = Book.objects.all()
        num_books = Book.objects.all().count()
        num_instances =  BookInstance.objects.all().count()
        num_authors = Author.objects.all().count()
        authors = Author.objects.all()

        books_avaiables = BookInstance.objects.filter(status__exact="a").count

        return render(
            request,
            "library.html", 
            context={
                "num_books": num_books,
                "books": books,
                "num_instances": num_instances,
                "num_authors": num_authors,
                "authors": authors,
                "books_avaiables": books_avaiables,
                "username":username

            }
        )
    else:
        return redirect('login')

