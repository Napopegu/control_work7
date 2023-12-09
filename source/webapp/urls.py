from django.urls import path
from webapp.views import guests_book_view,guest_add_view

urlpatterns = [
path('',guests_book_view, name='index'),
path('guests/add/',guest_add_view, name='guest_add_view' )
]