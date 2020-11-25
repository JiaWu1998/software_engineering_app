from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    # remember checks for constrict in the input form with postal code, credit card number, CVV
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    street = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    postal_code = models.CharField(max_length=5) #check
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=320)
    password = models.CharField(max_length=50)

    #Card Information
    name_on_card = models.CharField(max_length=30)
    credit_card_number = models.CharField(max_length=16) #check
    cvv_number = models.CharField(max_length=3) #check
    billing_street = models.CharField(max_length=35)
    billing_city = models.CharField(max_length=35)
    billing_state = models.CharField(max_length=35)
    billing_postal_code = models.CharField(max_length=5) #check

    #Point System
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name} ,Customer Id: {str(self.customer_id)}'

class Order_history(models.Model):
    customer_id = models.IntegerField()
    staff_id = models.IntegerField()
    # item_list is a string dictionary that has all items ordered, quanity of each item, and price per item
    item_list = models.CharField(max_length=500)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Customer Id: {str(self.customer_id)} ,Item_list: {self.item_list}'

class Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=320)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Item: {self.item_name} ,Item Id: {str(self.item_id)}'

class Credit_card(models.Model):
    credit_card_number = models.CharField(max_length=16)
    payment_name = models.CharField(max_length=26)
    name_on_card = models.CharField(max_length=30)
    cvv_number = models.CharField(max_length=3) 
    billing_street = models.CharField(max_length=35)
    billing_city = models.CharField(max_length=35)
    billing_state = models.CharField(max_length=35)
    billing_postal_code = models.CharField(max_length=5) 

    def __str__(self):
        return f'Number: {self.credit_card_number} ,Name: {self.payment_name}'

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    street = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    postal_code = models.CharField(max_length=5) 
    email = models.EmailField(max_length=320)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=35)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name} ,Staff Id: {str(self.staff_id)}'