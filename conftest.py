import pytest
from main import BooksCollector

@pytest.fixture
def create_object():
    book = BooksCollector()
    return book

@pytest.fixture
def new_book(create_object):
    create_object.add_new_book('Крутая книга')
    return create_object