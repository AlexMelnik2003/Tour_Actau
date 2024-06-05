from django import forms
from .models import Book_list, Faq

from django import forms
from .models import Book_list


class BookingForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    number_phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}))

    class Meta:
        model = Book_list
        fields = ['first_name', 'last_name', 'number_phone']


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['questions']
        widgets = {
            'questions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Напишите сюда вопрос или предложение'}),
        }

