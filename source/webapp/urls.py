from django.urls import path
from webapp.views import guests_book_view,guest_add_view, guest_update_view,guest_delete_view

urlpatterns = [
path('',guests_book_view, name='index'),
path('guests/add/',guest_add_view, name='guest_add_view' ),
path('guests/<int:pk>/update/',guest_update_view, name='guest_update_view' ),
path('guests/<int:pk>/delete/',guest_delete_view, name='guest_delete_view' )
]