from django.db import models

"""
This represents a Restaurant and Customer Integation system, which helps customers to preorder
their meal, before they arrive at the restaurant.
"""
class Customer(models.Model):
    class Meta:
        unique_together = (('username', 'email'),)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20, primary_key=True)


class Owner(models.Model):
    class Meta:
        unique_together = (('username', 'email'),)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20, primary_key=True)    

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=80)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Order(models.Model):
    orderTime = models.DateTimeField(auto_now_add=True, blank=True)
    pickupTime = models.DateTimeField(auto_now_add=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Food(models.Model):
    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'
    
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    prepTime = models.IntegerField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Table(models.Model):
    isOccupied = models.BooleanField(default=False)
    capacity = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

