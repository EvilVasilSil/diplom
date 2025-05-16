from django import forms
from .models import Expense, Category
from django.db.models import Q

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'category', 'date']
        labels = {
            'amount': 'Сумма',
            'description': 'Описание',
            'category': 'Категория',
            'date': 'Дата'
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(
            Q(user=user) | Q(user__isnull=True))
        self.fields['category'].empty_label = "Выберите категорию"
        
        # Стилизация полей
        self.fields['amount'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите сумму'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название категории'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }