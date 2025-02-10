from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.timezone import now

from accounts.models import User
from .permissions import (
    IsAuthenticatedAdmin,
    IsAuthenticatedBuyer
)

from ..models import (
    Book,
    Category,
    BuyBookNumber
)
from .serializers import (
    CategorySerializer,
    BuyBookSerializer
)



class CategoryMixinsView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


'''

{
    "name": "Riyazi"
}

'''


class CategoryDetailMixinsView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ListBookMixinsView(mixins.ListModelMixin,
                        generics.GenericAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)



class CreateBookMixinsView(mixins.CreateModelMixin,
                        generics.GenericAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CreateDetailMixinsView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class BuyBookAPIView(APIView):
    permission_classes = [IsAuthenticatedBuyer]

    def get_book_object(self, pk):
        book = Book.objects.select_related('category').filter(id=pk)
        
        return book
    
    def get_buyer_object(self, request):
        buyer = request.user

        return buyer
    
    def get_admin_object(self):
        admin = User.objects.filter(is_employee=1)

        return admin
    
    def post(self, request, pk):
        book = self.get_book_object(pk=pk)
        buyer = self.get_buyer_object(request=request)
        admin = self.get_admin_object()

        serializer = BuyBookSerializer(data=request.data)

        if serializer.is_valid():
            order_number = serializer.validated_data.get('number')
            stock_number = book.number

            if stock_number > 0 and stock_number >= order_number:
                buyer_balance = buyer.account_balance
                admin_balance = admin.account_balance
                now_datetime = now()

                if book.offer_price != 0 and book.offer_dedline > now_datetime:
                    book_price = book.offer_price
                else:
                    book_price = book.price
                
                amount = book_price * order_number

                if buyer.account_balance == None:
                    buyer_balance = 0
                else:
                    buyer_balance = buyer.account_balance

                if admin.account_balance == None:
                    admin_balance = 0
                else:
                    admin_balance = admin.account_balance
                
                if buyer_balance >= amount:
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

                    return Response({'detail': f'{order_number} ədəd {book.title} adlı kitab alındı'}, status=status.HTTP_200_OK)
                
                
                return Response({'detail': 'Balansınızda kifayət qədər vəsait yoxdur'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'detail': 'Stokda kifayət qədər kitab yoxdur'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Form yanlışdır'}, status=status.HTTP_400_BAD_REQUEST)

'''

{
    "number": 2
}

'''