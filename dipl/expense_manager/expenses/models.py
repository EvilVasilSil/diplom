from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    DEFAULT_CATEGORIES = [
        ('RESTAURANT', 'Рестораны'),
        ('AUTO', 'Авто'),
        ('HOTELS', 'Отели'),
        ('TICKETS', 'Билеты'),
    ]

    name = models.CharField(_('Название'), max_length=100)
    user = models.ForeignKey(
        User, 
        verbose_name=_('Пользователь'), 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )

    def get_name_display(self):
        return dict(self.DEFAULT_CATEGORIES).get(self.name, self.name)
    
    name = models.CharField(max_length=100, choices=DEFAULT_CATEGORIES, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.get_name_display()

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.category} - {self.date}"
    




    