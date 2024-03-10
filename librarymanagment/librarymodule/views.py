from django.shortcuts import render
from .models import *
# Create your views here.
def librarybooks(request):
    return render(request, 'librarymodule/librarybooks.html')
def add_Book_Details(request):
    if request.method == 'POST':
        Book_title=request.POST.get('BookTitle')
        Book_price=request.POST.get('BookPrice')
        Book_type=request.POST.get('BookType')
        Book_Author=request.POST.get('BookAuthor')
        About=request.POST.get('About')
        Books_Details= BooksDetails(
            Book_title=Book_title,
            Book_price=Book_price,
            Book_type=Book_type,
            Book_Author=Book_Author,
            About=About,
        )
        Books_Details.save()
        return render(request, 'librarymodule/datainserted.html')
    return render(request,'libraryhomepage.html')
def view_book_details(request):
    book_details_list= BooksDetails.objects.all()
    return render(request,'librarymodule/view_books.html',{'book_details_list':book_details_list})

