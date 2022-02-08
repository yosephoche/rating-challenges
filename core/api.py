from typing import List

from asgiref.sync import sync_to_async
from ninja import NinjaAPI

from core.Schemas import BookSchema, CreateBookSchema, BookDetailSchema, BookRatingSchema, AddRatingSchema
from core.models import Book, BookRating
from core.usecases import RateUseCase

api = NinjaAPI()


@api.post("/add-book", response=BookSchema)
def add_book(request, payload: CreateBookSchema):
    book = Book.objects.create(**payload.__dict__)
    return book


@api.get("/book-list", response=List[BookDetailSchema])
def get_book_list(request):
    books = Book.objects.all()
    result = []
    for book in books:
        book_schema = BookSchema(**book.__dict__)
        result.append(BookDetailSchema(book=book_schema))
    return result


@api.get("/book/detail/{book_id}", response=BookDetailSchema)
def get_detail(request, book_id: int):
    response = RateUseCase.get_book_with_review(book_id)
    return response


@api.post("/add-rating/{book_id}", response=BookRatingSchema)
def add_rating(request, book_id: int, payload: AddRatingSchema):
    response = RateUseCase.make_review(book_id, payload)

    return response
