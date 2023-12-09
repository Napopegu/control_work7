from django.urls import path
from webapp.views import guests_book_view

urlpatterns = [
path('',guests_book_view),
]