from django.test import TestCase
from book.models import Book, Category


class BookCategoryModelTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='horror')
        Book.objects.create(name='alone at home',
                            ISBN='978-3-16-148410-0',
                            category=cat)

    def test_book_is_created(self):
        '''checks if book is created'''
        book = Book.objects.get(name='alone at home')
        self.assertIsNotNone(book)

    def test_book_has_correct_isbn(self):
        '''checks if the correct isbn was stored for the book'''
        book = Book.objects.get(name='alone at home')
        self.assertEqual(book.ISBN, '978-3-16-148410-0')

    def test_book_has_category(self):
        '''checks if the book has a category of horror'''
        book = Book.objects.get(name='alone at home')
        self.assertEqual(book.category__name, 'horror')

    def test_category_exists(self):
        '''checks if horror category was created'''
        cat = Category.objects.get(name='horror')
        self.assertEqual(cat.name, 'horror')
