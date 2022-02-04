from typing import List

from asgiref.sync import sync_to_async
from ninja import NinjaAPI

from core.Schemas import BookSchema, CreateBookSchema, BookDetailSchema, BookRatingSchema, AddRatingSchema
from core.models import Book, BookRating

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
    book = Book.objects.filter(id=book_id).prefetch_related("Rating").first()
    book_schema = BookSchema(**book.__dict__)
    book_rate_schema = [BookRatingSchema(**rating.__dict__) for rating in book.Rating.all()]
    rate = round(sum(rating.rate for rating in book.Rating.all()) / len(book.Rating.all()), 2)
    return BookDetailSchema(book=book_schema, rate=rate, ratings=book_rate_schema)


@api.post("/add-rating/{book_id}", response=BookRatingSchema)
def add_rating(request, book_id: int, payload: AddRatingSchema):
    book = Book.objects.filter(id=book_id).first()
    book_rate = BookRating.objects.create(fk_book=book, rate=payload.rate, review=payload.review)

    return BookRatingSchema(**book_rate.__dict__)