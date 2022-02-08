from core.exceptions import object_not_found, ratings_not_found
from core.Schemas import BookRatingSchema, AddRatingSchema, BookSchema, BookDetailSchema
from core.models import Book, BookRating


class RateUseCase:
    @staticmethod
    def get_book_with_review(book_id: int):
        book = Book.objects.filter(id=book_id).prefetch_related("Rating").first()

        if not book:
            raise object_not_found()

        ratings = book.Rating.all()
        rate = 0

        if ratings:
            rate = round(sum(rating.rate for rating in ratings) / len(ratings), 1)

        book_rate_schema = [BookRatingSchema(**rating.__dict__) for rating in ratings]

        book_schema = BookSchema(**book.__dict__)

        return BookDetailSchema(book=book_schema, rate=rate, ratings=book_rate_schema)

    @staticmethod
    def make_review(book_id: int, payload: AddRatingSchema):
        book = Book.objects.filter(id=book_id).first()

        if not book:
            raise object_not_found()

        book_rate = BookRating.objects.create(fk_book=book, rate=payload.rate, review=payload.review)

        return BookRatingSchema(**book_rate.__dict__)

