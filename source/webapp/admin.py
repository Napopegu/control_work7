from django.contrib import admin
from webapp.models import  Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register your models here.
