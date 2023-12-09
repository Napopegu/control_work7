from django.shortcuts import render
from webapp.models import Book

def guests_book_view(request):
    guests_book = Book.objects.all()
    return render(request, template_name='guests_list.html', context={'guests': guests_book})