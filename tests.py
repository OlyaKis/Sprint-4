import pytest
from main import BooksCollector
from conftest import create_object
from conftest import new_book

class TestBooksCollector:

    @pytest.mark.parametrize('name',
    [
        'Интересная книга',
        'Скучная книга',
        'Захватывающая книга'
    ])
    def test_add_new_books_add_three_book(self, name, create_object):
        create_object.add_new_book(name)
        assert name in create_object.books_genre

    def test_add_new_book_set_correct_genre(self, create_object, new_book):
        create_object.set_book_genre('Крутая книга', 'Фантастика')
        fantasy_list = create_object.get_books_with_specific_genre('Фантастика')
        assert 'Крутая книга' in fantasy_list

    def test_check_quantity_books_in_one_genre(self, create_object):
        create_object.add_new_book('Книга 1')
        create_object.add_new_book('Книга 2')
        create_object.set_book_genre('Книга 1', 'Мультфильмы')
        create_object.set_book_genre('Книга 2', 'Мультфильмы')
        cartoon_list = create_object.get_books_with_specific_genre('Мультфильмы')
        assert len(cartoon_list) == 2

    def test_check_books_for_children_dont_include_adult_horror_books(self, create_object):
        create_object.add_new_book('Страшная книга')
        create_object.set_book_genre('Страшная книга', 'Ужасы')
        children_books = create_object.get_books_for_children()
        assert 'Страшная книга' not in children_books

    def test_check_books_for_children_include_only_children_genres(self, create_object):
        create_object.add_new_book('Детская книга')
        create_object.add_new_book('Ужасная книга')
        create_object.set_book_genre('Детская книга', 'Мультфильмы')
        create_object.set_book_genre('Ужасная книга', 'Ужасы')
        children_books = create_object.get_books_for_children()
        assert children_books == ['Детская книга']

    def test_new_books_dont_have_genre(self, create_object):
        create_object.add_new_book('Книга Раз')
        assert create_object.get_book_genre('Книга Раз') == ''

    def test_add_book_in_favorites(self, new_book):
        new_book.add_book_in_favorites('Крутая книга')
        assert 'Крутая книга' in new_book.favorites

    def test_get_book_genre_by_book_name(self, create_object):
        create_object.add_new_book('Веселая книга')
        create_object.set_book_genre('Веселая книга', 'Комедии')
        check_genre = create_object.get_book_genre('Веселая книга')
        assert check_genre == 'Комедии'

    def test_empty_list_books_genre_before_adding_new_books(self, create_object):
        assert create_object.get_books_genre() == {}

    def test_delete_book_from_favorites(self, create_object):
        create_object.add_new_book('Крутая книга')
        create_object.add_book_in_favorites('Крутая книга')
        create_object.delete_book_from_favorites('Крутая книга')
        assert 'Крутая книга' not in create_object.get_list_of_favorites_books()

    def test_empty_list_favourites_before_adding_books(self, create_object):
        assert create_object.get_list_of_favorites_books() == []