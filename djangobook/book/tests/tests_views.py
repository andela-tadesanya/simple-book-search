from django.test import TestCase
from django.core.urlresolvers import reverse
from book.models import Book, Category


class SearchViewTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='horror')
        Book.objects.create(name='alone at home',
                            ISBN='978-3-16-148410-0',
                            category=cat)

    def test_search_view_get_returns(self):
        '''checks if search view returns 200 status code'''
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('book/search.html')

    def test_search_view_post_returns(self):
        '''checks a post call to search view returns 200 status code'''
        response = self.client.post(reverse('search'), {'query': 'alone', 'parameter': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('book/result.html')
