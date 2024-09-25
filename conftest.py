import pytest

from main import BooksCollector

@pytest.fixture
def new_book():
    book = BooksCollector()
    book.add_new_book('Крутая книга')
    return book