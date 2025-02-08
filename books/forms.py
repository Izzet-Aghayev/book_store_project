from django import forms

from .models import (
    Book,
    BuyBookNumber,
    Category
)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['name'].label = 'Kateqoriya əlavə edin'



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['category'].label = 'Kateqoriya seçin'
        self.fields['title'].label = 'Kitabın adını əlavə edin'
        self.fields['author'].label = 'Kitabın müəllifini əlavə edin'
        self.fields['price'].label = 'Kitabın ilk qiymətini əlavə edin'
        self.fields['offer_price'].label = 'Kitabın endirimli qiymətini əlavə edin'
        self.fields['offer_dedline'].label = 'Endirimin bitmə zamanını əlavə edin'
        self.fields['number'].label = 'Kitabın sayını əlavə edin'
        self.fields['book_isbn'].label = 'Kitabın isbn-ini əlavə edin'
        self.fields['description'].label = 'Kitab haqqında məlumat yazın'
        self.fields['book_image'].label = 'Kitabın şəklini əlavə edin'



class BuyBookForm(forms.ModelForm):
    class Meta:
        model = BuyBookNumber
        fields = ('number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['number'].label = 'Neçə ədəd kitab almaq istəyirsiz?'