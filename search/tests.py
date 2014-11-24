from django.test import TestCase
from django.test.client import Client
from .views import _search_twitter, _search_wikipedia
from .forms import SearchForm

# Create your tests here.
class SearchPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_page_GET_200(self):
        """A GET request for the search page should always return an HTTP 200 OK"""
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_search_post(self):
        """A POST request to the search page"""

        # A proper search on Twitter and Wikipedia
        response = self.client.post('/', {'q': 'search', 'source': 'both'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # A search without source
        response = self.client.post('/', {'q': 'search', 'source': ''})
        # Check that the response is not a 200 OK.
        self.assertNotEqual(response.status_code, 200)
        # Check that the response is not a 500 INTERNAL SERVER ERROR.
        self.assertNotEqual(response.status_code, 500)

        # A Twitter search with no query
        response = self.client.post('/', {'q': '', 'source': 'twitter'})
        # Check that the response is a 200 OK.
        self.assertEqual(response.status_code, 200)

        # A Wikipedia search
        response = self.client.post('/', {'q': 'test', 'source': 'wikipedia'})
        # Check that the response is a 200 OK.
        self.assertEqual(response.status_code, 200)

    # Will raise an exception if improperly configured or service is down
    def test_search_twitter(self):
        _search_twitter("search")

    # Will raise an exception if improperly configured or service is down
    def test_search_wikipedia(self):
        _search_wikipedia("search")