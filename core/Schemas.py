from typing import List

from ninja import Schema, ModelSchema

from core.models import Book, BookRating


class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = "__all__"


class BookRatingSchema(ModelSchema):
    class Config:
        model = BookRating
        model_fields = "__all__"


class BookDetailSchema(Schema):
    book: BookSchema
    rate: float = 0.0
    ratings: List[BookRatingSchema] = []


class CreateBookSchema(BookSchema):
    class Config(BookSchema.Config):
        model_fields = ["title", "description", "author"]


class AddRatingSchema(Schema):
    rate: float
    review: str

