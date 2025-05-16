from django.urls import path
from .views import (
    ExpenseListView,
    ExpenseCreateView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    CategoryCreateView,
)

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('new/', ExpenseCreateView.as_view(), name='expense_create'),
    path('edit/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('categories/new/', CategoryCreateView.as_view(), name='category_create'),
]
