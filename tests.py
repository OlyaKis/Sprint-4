import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('name',
    [
        'Интересная книга',
        'Скучная книга',
        'Захватывающая книга'
    ])
    def test_add_new_books_add_three_book(self, name):
        book = BooksCollector()
        book.add_new_book(name)
        assert name in book.books_genre

    def test_add_new_book_set_correct_genre(self, new_book):
        new_book.set_book_genre('Крутая книга', 'Фантастика')
        fantasy_list = new_book.get_books_with_specific_genre('Фантастика')
        assert 'Крутая книга' in fantasy_list

    def test_check_quantity_books_in_one_genre(self):
        book = BooksCollector()
        book.add_new_book('Первая книга')
        book.add_new_book('Вторая книга')
        book.add_new_book('Третья книга')
        book.set_book_genre('Первая книга', 'Мультфильмы')
        book.set_book_genre('Вторая книга', 'Мультфильмы')
        book.set_book_genre('Третья книга', 'Мультфильмы')
        cartoon_list = book.get_books_with_specific_genre('Мультфильмы')
        assert len(cartoon_list) == 3

    def test_check_books_for_children_dont_include_adult_horror_books(self, new_book):
        new_book.set_book_genre('Крутая книга', 'Ужасы')
        children_books = new_book.get_books_for_children()
        assert 'Страшная книга' not in children_books

    def test_check_books_for_children_include_only_children_genres(self, new_book):
        new_book.set_book_genre('Детективная книга', 'Детективы')
        new_book.set_book_genre('Ужасная книга', 'Ужасы')
        children_books = new_book.get_books_for_children()
        assert children_books == []

    def test_new_books_dont_have_genre(self, new_book):
        new_book.add_new_book('Книга Раз')
        assert 'Книга Раз' not in new_book.genre

    def test_add_book_in_favorites(self, new_book):
        new_book.add_book_in_favorites('Крутая книга')
        assert 'Крутая книга' in new_book.favorites

    def test_get_book_genre_by_book_name(self, new_book):
        new_book.set_book_genre('Крутая книга', 'Комедии')
        check_genre = new_book.get_book_genre('Крутая книга')
        assert check_genre == 'Комедии'

    def test_empty_list_books_genre_before_adding_new_books(self):
        book = BooksCollector()
        assert book.get_books_genre() == {}

    def test_delete_book_from_favorites(self, new_book):
        new_book.add_book_in_favorites('Крутая книга')
        new_book.delete_book_from_favorites('Крутая книга')
        assert 'Крутая книга' not in new_book.favorites

    def test_empty_list_favourites_before_adding_books(self):
        book = BooksCollector()
        assert book.get_list_of_favorites_books() == []