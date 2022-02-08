from ninja import NinjaAPI
from ninja.errors import HttpError

api = NinjaAPI()


class BaseCustomException(Exception):
    pass


# initializing handler

@api.exception_handler(BaseCustomException)
def object_not_found():
    raise HttpError(400, "Can't find object")


@api.exception_handler(BaseCustomException)
def ratings_not_found():
    raise HttpError(400, "Rating is empty")
