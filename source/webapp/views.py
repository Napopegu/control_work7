from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Book

def guests_book_view(request):
    guests_book = Book.objects.all().order_by('date_start').filter(status='active')
    return render(request, template_name='guests_list.html', context={'guests': guests_book})

def guest_add_view(request):
    if request.method =="GET":
        guests_book = Book.objects.all()
        return render(request, template_name='guest_create.html', context={'guests': guests_book})
    elif request.method =="POST":
        guests_book = Book.objects.create(
            author_name=request.POST.get('title'),
            author_mail=request.POST.get('mail'),
            text=request.POST.get('description')
        )
        return redirect('index')

def guest_update_view(request, pk):
    guests_book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        # guest = Book.objects.all()
        return render(request, template_name='guest_update.html', context={'guests': guests_book})
    elif request.method == "POST":
        guests_book.author_name=request.POST.get('title')
        guests_book.author_mail=request.POST.get('mail')
        guests_book.text=request.POST.get('description')
        guests_book.save()

        return redirect('index')

def guest_delete_view(request, pk):
    guests_book = get_object_or_404(Book, pk=pk)
    guests_book.delete()
    return redirect('index')
