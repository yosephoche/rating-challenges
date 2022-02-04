from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BookRating(models.Model):
    fk_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="Rating")
    review = models.TextField()
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.fk_book.title


