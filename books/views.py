from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from accounts.models import Profile, User

from .models import (
    Book,
    BuyBookNumber
)

from .forms import (
    BookForm,
    BuyBookForm
)

class ListBookViews(View):
    def get(self, request):
        books = Book.objects.all()
        now_datetime = datetime.now().strftime("%d-%m-%Y %H:%M")

        context = {
            'books': books,
            'now_datetime': now_datetime
        }
        print(now_datetime)

        return render(request, 'books/home_page.html', context)
    

class CreateBookView(LoginRequiredMixin, View):
    def get_user(self, request):
        user = request.user
        return user

    def get(self, request):
        user = self.get_user(request=request)
        book_form = BookForm()

        context = {
            'book_form': book_form
        }
        
        if user.is_employee == 1:
            return render(request, 'books/create_book.html', context)
        else:
            messages.info(request, 'Yalnız inzibatçı elan yarada bilər')
            return redirect('all_books')
    
    def post(self, request):
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()

            messages.success(request, 'Kitab elanı uğurla yaradıldı')
            return redirect('create_book')
        
        else:
            messages.error(request, book_form.errors)
            return redirect('create_book')


class DetailBookView(LoginRequiredMixin, View):
    def get_object(self, pk):
        books = Book.objects.select_related('category')
        book = get_object_or_404(books, pk=pk)
        return book

    def get(self, request, pk):
        book = self.get_object(pk=pk)

        context = {
            'book': book,
        }

        return render(request, 'books/detail_book.html', context)
    
    def post(self, request, pk):
        book = self.get_object(pk=pk)

        context = {
            'book': book,
        }

        return render(request, 'books/detail_book.html', context)


class UpdateBookView(LoginRequiredMixin, View):
    def get_object(self, pk):
        books = Book.objects.select_related('category')
        book = get_object_or_404(books, pk=pk)
        return book

    def get_user(self, request):
        user = request.user
        return user
    
    def get(self, request, pk):
        user = self.get_user(request=request)
        book = self.get_object(pk=pk)
        book_form = BookForm(instance=book)
        context = {
            'book_form': book_form
        }

        if user.is_employee == 1:
            return render(request, 'books/update_book.html', context)
        else:
            messages.info(request, 'Yalnız inzibatçı dəyişiklik edə bilər')
            return redirect('all_books')
    
    def post(self, request, pk):
        book = self.get_object(pk=pk)
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('detail_book', book.id)
        else:
            messages.error(request, book_form.errors)
            return redirect('update_book', book.id)
        

class DeleteBookView(LoginRequiredMixin, View):
    def get_object(self, pk):
        books = Book.objects.select_related('category')
        book = get_object_or_404(books, pk=pk)
        return book
    
    def get_user(self, request):
        user = request.user
        return user

    def get(self, request, pk):
        user = self.get_user(request=request)
        book = self.get_object(pk=pk) 
        if user.is_employee==1:
            self.perform_delete(obj=book)
            messages.success(request, f'{book.title} adlı kitab elanı silindi.')
            return redirect('all_books')
        else:
            messages.info(request, 'Yalnız inzibatçı silinmə edə bilər')
            return redirect('all_books')
        
    def perform_delete(self, obj):
        obj.delete()



class BuyBook(LoginRequiredMixin, View):
    def get_book_object(self, pk):
        books = Book.objects.select_related('category')
        book = get_object_or_404(books, pk=pk)

        return book

    def get_buyer(self, request):
        buyer = request.user
        profiles = Profile.objects.select_related('user')
        profile = get_object_or_404(profiles, user=buyer)

        return profile
    
    def get_admin(self):
        admin = User.objects.filter(is_employee=1)
        profiles = Profile.objects.select_related('user')
        profile = get_object_or_404(profiles, user=admin.first())

        return profile
    
    def get_user(self, request):
        user = request.user
        return user

    def get(self, request, pk):
        user = self.get_user(request=request)
        book = self.get_book_object(pk=pk)
        form = BuyBookForm()
        context = {
            'book': book,
            'form': form
        }

        if user.is_employee == 0:
            return render(request, 'books/buy_book.html', context)
        else:
            messages.info(request, 'Yalnız alıcı kitab ala bilər')
            return redirect('all_books')
        

    def post(self, request, pk):
        previous_page = request.POST.get("previous_page")

        book = self.get_book_object(pk=pk)
        buyer = self.get_buyer(request=request)
        admin = self.get_admin()

        form = BuyBookForm(request.POST)

        if form.is_valid():
            order_books = form.save(commit=False)
            order_number = order_books.number
            stock_number = book.number
            if stock_number >= order_number:
                amount = book.offer_price * order_number
                
                if buyer.account_balance == None:
                    buyer_balance = 0
                else:
                    buyer_balance = buyer.account_balance

                if admin.account_balance == None:
                    admin_balance = 0
                else:
                    admin_balance = admin.account_balance

                if buyer.account_balance >= amount:
                    new_buyer_balance = buyer_balance - amount
                    new_admin_balance = admin_balance + amount
                    new_number_books = book.number - order_number

                    buyer.account_balance = new_buyer_balance
                    admin.account_balance = new_admin_balance
                    book.number = new_number_books

                    buyer.save()
                    admin.save()
                    book.save()

                    BuyBookNumber.objects.create(book=book, number=order_number)

                    messages.success(request, f'{order_number} ədəd {book.title} adlı kitab alındı')
                    return redirect(previous_page)
                
                messages.info(request, 'Balansınızda kifayət qədər vəsait yoxdur')
                return redirect(previous_page)
            
            messages.info(request, 'Stokda kifayət qədər kitab yoxdur')
            return redirect(previous_page)
        
        messages.error(request, 'Form yanlışdır')
        return redirect(previous_page)
