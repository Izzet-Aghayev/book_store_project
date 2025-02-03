from django import forms

from .models import (
    Book,
    BuyBookNumber
)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'



class BuyBookForm(forms.ModelForm):
    class Meta:
        model = BuyBookNumber
        fields = ('number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        
        self.fields['number'].label = 'Neçə ədəd kitab almaq istəyirsiz?'