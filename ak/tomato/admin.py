from django.contrib import admin
from .models import FoodOrder, FoodOrderAdmin

admin.site.register(FoodOrder, FoodOrderAdmin)