from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Expense, Category
from .forms import ExpenseForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy('expense_list')

    # Добавляем user в аргументы формы
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Аналогично для ExpenseUpdateView

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense  # Указываем модель
    form_class = ExpenseForm  # Используем нашу форму
    template_name = 'expenses/expense_form.html'  # Шаблон формы
    success_url = reverse_lazy('expense_list')  # Куда перенаправить после успеха

    # Добавляем user в форму
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

from django.views.generic import DeleteView

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense  # Указываем модель
    template_name = 'expenses/expense_confirm_delete.html'  # Шаблон подтверждения
    success_url = reverse_lazy('expense_list')  # Перенаправление после удаления

    # Для проверки прав доступа
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('expense_list')