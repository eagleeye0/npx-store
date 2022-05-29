from django.db import models

# Create your models here.


# class ParentCategory(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     category_name = models.CharField(max_length=50)
#     url_slug = models.SlugField(max_length=20)
#     default_photo = models.ImageField(
#         upload_to='photos/categories', blank=True)
#     description = models.CharField(max_length=200)
#     parent_category = models.ForeignKey(
#         ParentCategory, on_delete=models.RESTRICT)

#     def __str__(self):
#         return self.category_name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table = "customer"


# class Seller(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     password_hash = models.CharField(max_length=100)
#     profile_photo = models.ImageField(upload_to='photos/sellers')

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     product_name = models.CharField(max_length=50)
#     url_slug = models.SlugField(max_length=20)
#     seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.product_name


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
