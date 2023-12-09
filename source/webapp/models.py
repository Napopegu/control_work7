from django.db import models

class Book(models.Model):
    STATUS = [
        ('active','Активно'),
        ('blocked','Блокировано')
    ]
    author_name = models.CharField(max_length=50, verbose_name="Имя автора записи")
    author_mail = models.EmailField(max_length=100, verbose_name="Почта автора записи")
    text = models.TextField(max_length=200, verbose_name="Текст записи")
    date_start = models.DateTimeField(auto_now_add=True, verbose_name="время создания")
    date_edit = models.DateTimeField(auto_now=True, verbose_name="время редактирования")
    status = models.CharField(max_length=25, default="active",choices=STATUS, verbose_name='Статус')
