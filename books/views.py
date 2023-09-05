from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404,redirect
import json
from books.models import Book, Review
from django.http import Http404
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from books.form import ReviewForm

booksData = open(r"C:\Users\Muhammad Umair\Documents\django\bookstore\books.json").read()


data= json.loads(booksData)


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()
    
class BookDetailView(DetailView):
    model=Book
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["reviews"]= context['book'].review_set.order_by('-created_at')
        context["authors"]= context['book'].authors.all()
        context["form"]= ReviewForm()
        return context

def review(request,id):
    if request.user.is_authenticated:
        newReview= Review(book_id=id,user=request.user)
        form= ReviewForm(request.POST,request.FILES,instance=newReview)
        if form.is_valid():
            form.save()
    return redirect(f'/book/{id}')

def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context= {'book_list': books}
    return render(request, 'books/book_list.html',context)
