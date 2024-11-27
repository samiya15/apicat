from django.db import models
from customer.models import customer
# Create your models here.

class Order(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE, related_name='orders')
    order_date=models.DateTimeField(auto_now_add=True)
    order_total=models.DecimalField(max_digits=10,decimal_places=2)
    
    def _str_(self):
        return self.customer.first_name +" " +self.customer.last_name +" "+str(self.order_total)
    