from django import forms
from .models import Book_list, Faq

from django import forms
from .models import Book_list


class BookingForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия и имя'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}))
    number_phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}))

    class Meta:
        model = Book_list
        fields = ['name', 'email', 'number_phone']


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['questions']
        widgets = {
            'questions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Напишите сюда вопрос или предложение'}),
        }

