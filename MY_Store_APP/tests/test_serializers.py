import pytest
from MY_Store_APP.Grocery.serializers import CategorySerializer, ProductSerializer, UserSerializer, OrderSerializer

@pytest.mark.django_db
def test_category_serializer():
    data = {'name': 'Test Category', 'description': 'Test Description'}
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_product_serializer():
    data = {'name': 'Test Product', 'price': 10.99}
    serializer = ProductSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_user_serializer():
    data = {'username': 'name', 'email': 'test@example.com', 'password': 'password123', 'address': '123 Test St'}
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_order_serializer():
    user_data = {'username': 'name', 'email': 'test@example.com', 'password': 'password123', 'address': '123 Test St'}
    user_serializer = UserSerializer(data=user_data)
    user_serializer.is_valid()
    user_instance = user_serializer.save()
    product_data = {'name': 'Test Product', 'price': 10.99}
    product_serializer = ProductSerializer(data=product_data)
    product_serializer.is_valid()
    product_instance = product_serializer.save()
    order_data = {'customer': user_instance.id, 'products': [product_instance.id], 'total_price': 50.00, 'status': 'PENDING'}
    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid()

