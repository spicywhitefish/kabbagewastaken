from django.test import TestCase
from django.test.client import Client


# Create your tests here.
class SearchPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_page_GET_200(self):
        """A GET request for the search page should always return an HTTP 200 OK"""
        # Issue a GET request.
        from django.conf.global_settings import DATABASES
        print(DATABASES)
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)