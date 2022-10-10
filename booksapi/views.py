from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.http import QueryDict
# Create your views here.

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title');
        author = request.POST.get('author');
        price = request.POST.get('price');
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        # data = serialize("json", book)
        # return HttpResponse(data, content_type="application/json")
        return JsonResponse(model_to_dict(book), status=201)

@csrf_exempt
def book(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        return JsonResponse(model_to_dict(book))
    elif request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        reqbody = QueryDict(request.body)
        title = reqbody.get('title');
        author = reqbody.get('author');
        price = reqbody.get('price');
        if title:
            book.title = title
        if author:
            book.author = author
        if price:
            book.price = price 

        book.save()
        
        return JsonResponse(model_to_dict(book))

