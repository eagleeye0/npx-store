from pyexpat import model
from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=200)
    reset_otp = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = "customer"


class Seller(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    # profile_photo = models.ImageField(upload_to='photos/sellers')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'seller'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    mrp_price = models.FloatField()
    sale_price = models.FloatField()
    stock = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'


# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     order_date = models.DateField()
#     order_status = models.CharField(max_length=50)

#     def __str__(self):
#         return self.customer.first_name + ' ' + self.customer.last_name + ' ' + self.product.product_name


# class Photo(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='photos/products')

#     def __str__(self):
#         return self.product.product_name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    session_id = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'cart'


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    address_type = models.CharField(max_length=30, choices=[(
        'home', 'home'), ('office', 'office'), ('other', 'other')])

    class Meta:
        db_table = 'customer_address'


class SubscibeList(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'subscribe_list'
