from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .models import Book
from .forms import BookForm



class ListBookViews(View):
    def get(self, request):
        books = Book.objects.all()

        context = {
            'books': books
        }

        return render(request, 'templates/books/home_page.html', context)
    

class CreateBookView(View):
    def get(self, request):
        book_form = BookForm()

        context = {
            'book_form': book_form
        }
        
        return render(request, 'books/create_book.html', context)
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Kitab elanı uğurla yaradıldı')
            return redirect('create_book')
        
        else:
            messages.error(request, form.errors)
            return redirect('create_book')


class DetailBookView(View):
    def get_object(self, pk):
        books = Book.objects.select_related('categories')
        book = get_object_or_404(books, pk=pk)
        return book

    def get(self, request, pk):
        book = self.get_object(pk=pk)

        context = {
            'book': book
        }

        return render(request, 'books/detail_book.html', context)
