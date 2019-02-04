from rest_framework import serializers
from ..models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'username')

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', 'email', 'username')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'location', 'owner')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'content', 'likes', 'dislikes', 'customer', 'restaurant')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','orderTime', 'pickupTime', 'customer', 'restaurant')

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id','name', 'description', 'prepTime', 'price', 'restaurant', 'order')

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id','isOccupied', 'capacity', 'restaurant')    
