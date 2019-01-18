from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name = 'fbv_book_list'),
    path('view/<int:pk>', views.book_view, name = 'fbv_book_view'),
    path('new/', views.book_create, name = 'fbv_book_new'),
    path('edit/<int:pk>', views.book_update, name = 'fbv_book_edit'),
    path('delete/<int:pk>', views.book_delete, name = 'fbv_book_delete'),
]