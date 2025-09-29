from django.db import models
from django.contrib import admin
class Car_page(models.Model):
    name=models.CharField(max_length=40)
    colour=models.CharField(max_length=20)
    model=models.CharField(max_length=30)
    price=models.IntegerField()
    seat=models.IntegerField()

class Car_pageAdmin(admin.ModelAdmin):
    list_display=['name','colour','model','price','seat']
    
