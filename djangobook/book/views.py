from django.shortcuts import render
from .forms import SearchForm
from .models import Category, Book
from django.contrib import messages
from django.http import HttpResponseRedirect


# helper functions
def search_by_name(query):
    books = Book.objects.filter(name__icontains=query)
    return books


def search_by_cat(query):
    books = Book.objects.filter(category__name__icontains=query)
    return books


def throw_error(request):
    messages.error(request, 'Invalid search entry.')
    return HttpResponseRedirect('/')


# Create your views here.
def search(request):
    if request.method == 'GET':
        return render(request, 'book/search.html')
    else:
        # validate submitted form
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            parameter = form.cleaned_data['parameter']

            if parameter == 'name':
                result = search_by_name(query)
                return render(request, 'book/result.html', {'query': query, 'books': result})
            elif parameter == 'category':
                result = search_by_cat(query)
                return render(request, 'book/result.html', {'query': query, 'books': result})
            else:
                throw_error(request)
        else:
            throw_error(request)
