from django.db import models
from store.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=150)
    division = models.CharField(max_length=20)
    district = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=20)
    account_no = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=20)  # Changed to CharField
    payable = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField
    totalbook = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
