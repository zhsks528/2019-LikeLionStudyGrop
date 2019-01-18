from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name = 'cbv_book_list'),
    path('view/<int:pk>', views.BookView.as_view(), name = 'cbv_book_view'),
    path('new/', views.BookCreate.as_view(), name = 'cbv_book_new'),
    path('edit/<int:pk>', views.BookUpdate.as_view(), name = 'cbv_book_edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name = 'cbv_book_delete'),
]