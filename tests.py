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

    def test_add_new_book_set_correct_genre(self):
        book = BooksCollector()
        book.add_new_book('Тестовая книга')
        book.set_book_genre('Тестовая книга', 'Фантастика')
        fantasy_list = book.get_books_with_specific_genre('Фантастика')
        assert 'Тестовая книга' in fantasy_list

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

    def test_check_books_for_children_dont_include_adult_horror_books(self):
        book = BooksCollector()
        book.add_new_book('Страшная книга')
        book.set_book_genre('Страшная книга', 'Ужасы')
        children_books = book.get_books_for_children()
        assert 'Страшная книга' not in children_books

    def test_check_books_for_children_dont_include_adult_detective_books(self):
        book = BooksCollector()
        book.add_new_book('Детективная книга')
        book.set_book_genre('Детективная книга', 'Детективы')
        children_books = book.get_books_for_children()
        assert 'Детективная книга' not in children_books

    def test_new_books_dont_have_genre(self):
        book = BooksCollector()
        book.add_new_book('Книга Раз')
        assert 'Книга Раз' not in book.genre

    def test_add_book_in_favorites(self):
        book = BooksCollector()
        book.add_new_book('Избранная книга')
        book.add_book_in_favorites('Избранная книга')
        assert 'Избранная книга' in book.favorites

    def test_get_book_genre_by_book_name(self):
        book = BooksCollector()
        book.add_new_book('Проверочная книга')
        book.set_book_genre('Проверочная книга', 'Комедии')
        check_genre = book.get_book_genre('Проверочная книга')
        assert check_genre == 'Комедии'

    def test_empty_list_books_genre_before_adding_new_books(self):
        book = BooksCollector()
        assert book.get_books_genre() == {}

    def test_delete_book_from_favorites(self):
        book = BooksCollector()
        book.add_new_book('Неизбранная книга')
        book.add_book_in_favorites('Неизбранная книга')
        book.delete_book_from_favorites('Неизбранная книга')
        assert 'Неизбранная книга' not in book.favorites

    def test_empty_list_favourites_before_adding_books(self):
        book = BooksCollector()
        assert book.get_list_of_favorites_books() == []