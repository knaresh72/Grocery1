from rest_framework import serializers
from .models import Category, Product, User, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'