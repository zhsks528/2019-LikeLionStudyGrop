from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from crud_cbv.models import CBV_Book


class BookList(ListView):
    model = CBV_Book

class BookView(DetailView):
    model = CBV_Book

class BookCreate(CreateView):
    model = CBV_Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('cbv_book_list')

class BookUpdate(UpdateView):
    model = CBV_Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('cbv_book_list')

class BookDelete(DeleteView):
    model = CBV_Book
    success_url = reverse_lazy('cbv_book_list')
