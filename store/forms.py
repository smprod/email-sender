from django import forms
from django.forms import (formset_factory)


class TextForm(forms.Form):
    subject = forms.CharField(
        label='Тема',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите тему письма'
        })
    )
    text = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите текст письма'
        })
    )
    

class EmailForm(forms.Form):
    name = forms.EmailField(
        label='Почты',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите почту на которую отправить'
        })
    )




EmailFormset = formset_factory(EmailForm)