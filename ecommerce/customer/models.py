from django.db import models

# Create your models here.
class customer(models.Model):
    first_name=models.CharField(max_lengths=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)

def __str__(self):
    return self.first_name +" "+self.last_name

"""
Represents a customer in the e-commerce system.
    Fields:
        - first_name: The first name of the customer.
        - last_name: The last name of the customer.
        - email: The email address of the customer (must be unique).
    """