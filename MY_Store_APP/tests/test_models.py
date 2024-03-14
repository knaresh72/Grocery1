from django.test import TestCase
from MY_Store_APP.Grocery.models import Category, Product, User, Order

class TestModels(TestCase):
    def test_category_model_str_method(self):
        category = Category.objects.create(name='Test Category', description='Test Description')
        self.assertEqual(str(category), 'Test Category')

    def test_product_model_str_method(self):
        product = Product.objects.create(name='Test Product', description='Test Description', price=10.99, quantity=5)
        self.assertEqual(str(product), 'Test Product')

    def test_user_model_str_method(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password123', address='123 Test St')
        self.assertEqual(str(user), 'testuser')

    def test_order_model_str_method(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password123', address='123 Test St')
        order = Order.objects.create(customer=user, total_price=50.00, status='PENDING')
        self.assertEqual(str(order), f'Order #{order.id} - {user.username}')