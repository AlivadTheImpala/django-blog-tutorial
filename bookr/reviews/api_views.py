#  api_views.py
#  we organize our api views into this file. Here we create a view that returns all our books.
#  well create a variable to hold all the books which we can then use to serialize the entire book.
#  the attributes within the Book model has already been serialized in serializers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


# @api_view()
# def first_api_view(request):
#     num_books = Book.objects.count()  # count the number of objects in the Book model
#     return Response({"num_books": num_books})  # then return the result.


@api_view()
def all_books(request):
    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)  # many=True indicates that the books object is a queryset or
    # a list of many objects
    return Response(book_serializer.data)
