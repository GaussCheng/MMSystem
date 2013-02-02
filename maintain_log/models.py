from django.db import models
from customer_management import Customer
from product_management import Product

class MaintainLog(models.Model):
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    code = models.CharField(max_length=50)
    manufacture_date = models.DateField
    carry_date = models.DateField
    bug_find_by_customer = models.TextField