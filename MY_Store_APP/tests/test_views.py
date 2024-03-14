from django.test import TestCase
from rest_framework.test import APIClient

class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_category_list_create_view(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_create_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_user_list_create_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_order_list_create_view(self):
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, 200)


