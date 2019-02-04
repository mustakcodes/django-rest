from django.urls import path, include
from .views import *

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'owners', OwnerViewSet, basename='owners')
router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'food', FoodViewSet, basename='food')
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = router.urls

"""urlpatterns = [
    path('customers/', CustomerList.as_view()),
    path('customers/detail/<pk>', CustomerDetail.as_view()),
    path('customers/update/<pk>', CustomerUpdate.as_view()),
    path('customers/delete/<pk>', CustomerDelete.as_view()),
    path('owners/', OwnerList.as_view()),
    path('owners/detail/<pk>', OwnerDetail.as_view()),
    path('owners/update/<pk>', OwnerUpdate.as_view()),
    path('owners/delete/<pk>', OwnerDelete.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/detail/<pk>', OrderDetail.as_view()),
    path('orders/update/<pk>', OrderUpdate.as_view()),
    path('orders/delete/<pk>', OrderDelete.as_view()),
    path('restaurants/', RestaurantList.as_view()),
    path('restaurants/detail/<pk>', RestaurantDetail.as_view()),
    path('restaurants/update/<pk>', RestaurantUpdate.as_view()),
    path('restaurants/delete/<pk>', RestaurantDelete.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/detail/<pk>', CommentDetail.as_view()),
    path('comments/update/<pk>', CommentUpdate.as_view()),
    path('comments/delete/<pk>', CommentDelete.as_view()),
    path('food/', FoodList.as_view()),
    path('food/detail/<pk>', FoodDetail.as_view()),
    path('food/update/<pk>', FoodUpdate.as_view()),
    path('food/delete/<pk>', FoodDelete.as_view()),
    path('tables/', TableList.as_view()),
    path('tables/detail/<pk>', TableDetail.as_view()),
    path('tables/update/<pk>', TableUpdate.as_view()),
    path('tables/delete/<pk>', TableDelete.as_view()),
]"""
