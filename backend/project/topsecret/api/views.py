from rest_framework import generics
from rest_framework import viewsets
from ..models import *
from .serializers import *


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class OwnerViewSet(viewsets.ModelViewSet):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()

class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
"""
*** Generic views is way ***

# Customer-related views
class CustomerCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    # Lists the object of a model
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


####################################################################################

# Owner-related views
class OwnerCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetail(generics.RetrieveAPIView):
    # Lists the object of a model
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

##################################################################################

# Order-related views
class OrderCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    # Lists the object of a model
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

##################################################################################

# Restaurant-related views
class RestaurantCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    # Lists the object of a model
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

##################################################################################

# Comment-related views
class CommentCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveAPIView):
    # Lists the object of a model
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

##################################################################################

# Food-related views
class FoodCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveAPIView):
    # Lists the object of a model
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

##################################################################################

# Table-related views
class TableCreate(generics.CreateAPIView):
    # Allows the creation of a new object
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableList(generics.ListAPIView):
    # Lists the objects of a model
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableDetail(generics.RetrieveAPIView):
    # Lists the objects of a model
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableUpdate(generics.UpdateAPIView):
    # Allows the update of the object
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableDelete(generics.DestroyAPIView):
    # Allows the delete of the object
    queryset = Table.objects.all()
    serializer_class = TableSerializer

##################################################################################
"""