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
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()

            messages.success(request, 'Kitab elanı uğurla yaradıldı')
            return redirect('create_book')
        
        else:
            messages.error(request, book_form.errors)
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
    
    def post(self, request, pk):
        book = self.get_object(pk=pk)

        context = {
            'book': book
        }

        return render(request, 'books/detail_book.html', context)


class UpdateBookView(View):
    def get_object(self, pk):
        books = Book.objects.select_related('categories')
        book = get_object_or_404(books, pk=pk)
        return book
    
    def get(self, request, pk):
        book = self.get_object(pk=pk)
        book_form = BookForm(instance=book)
        context = {
            'book_form': book_form
        }

        return render(request, 'books/update_book.html', context)
    
    def post(self, request, pk):
        book = self.get_object(pk=pk)
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('detail_book', book.id)
        else:
            messages.error(request, book_form.errors)
            return redirect('update_book', book.id)
        

class DeleteBookView(View):
    def get_object(self, pk):
        books = Book.objects.select_related('categories')
        book = get_object_or_404(books, pk=pk)
        return book

    def get(self, request, pk):
        book = self.get_object(pk=pk)
        self.perform_delete(obj=book)
        messages.success(request, f'{book.title} adlı kitab elanı silindi.')
        return redirect('all_books')
    
    def post(self, request, pk):
        book = self.get_object(pk=pk)
        self.perform_delete(obj=book)
        messages.success(request, f'{book.title} adlı kitab elanı silindi.')
        return redirect('all_books')

    def perform_delete(self, obj):
        obj.delete()