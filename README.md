# Ex01 Django ORM Web Application
# Date: 25-05-2026
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM

```
models.py 


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


admin.py

from django.contrib import admin
from .models import FoodOrder, FoodOrderAdmin

admin.site.register(FoodOrder, FoodOrderAdmin)

```

# OUTPUT

![alt text](<Screenshot 2026-05-25 205833.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
