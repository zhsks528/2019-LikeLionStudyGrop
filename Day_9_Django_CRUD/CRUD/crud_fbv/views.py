from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import FBV_Book

class FBV_BookForm(ModelForm):
    class Meta:
        model = FBV_Book
        fields = ['name', 'pages']

def book_list(request, template_name='crud_fbv/fbv_book_list.html'):
    book = FBV_Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_view(request, pk, template_name='crud_fbv/fbv_book_detail.html'):
    book = get_object_or_404(FBV_Book, pk=pk)    
    return render(request, template_name, {'object':book})

def book_create(request, template_name='crud_fbv/fbv_book_form.html'):
    form = FBV_BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fbv_book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='crud_fbv/fbv_book_form.html'):
    book = get_object_or_404(FBV_Book, pk=pk)
    form = FBV_BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('fbv_book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='crud_fbv/fbv_book_confirm_delete.html'):
    book = get_object_or_404(FBV_Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('fbv_book_list')
    return render(request, template_name, {'object':book})