from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

state_list = ( 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Maharashtra', 'Madhya Pradesh', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Telangana', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman & Nicobar', 'Chandigarh ', 'Dadra & Nagar Haveli', 'Daman & Diu', 'Lakshadweep', 'Puducherry ',)


STATE_CHOICES = [(state, state) for state in state_list]

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lacality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()     
    state = models.CharField(max_length=50, choices=STATE_CHOICES)

    def str(self):
        return str(self.id)


CATEGORY_CHOICES =  (
    ('M', 'Mobile'),
    ('L','Laptop'),
    ('TW', 'top_wear'), 
    ('BW','Bottom Wear'),
    )


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.product.selling_price * self.quantity




STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel'),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.id}-{self.user}"
    
    @property
    def total_cost(self):
        return self.product.selling_price * self.quantity
