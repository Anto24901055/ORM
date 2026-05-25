from django.db import models
from django.contrib import admin

class FoodOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    order_date = models.DateField()

    def __str__(self):
        return self.customer_name

class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','customer_name','email','phone','food_item','quantity','price','order_date')