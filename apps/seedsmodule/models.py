from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Seed(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='seeds/')
    description = models.TextField()
    
    sun_light = models.CharField(max_length=100) 
    watering = models.CharField(max_length=100)  
    
    planting_month = models.IntegerField(help_text="Month number from 1 to 12")

    def __str__(self):
        return self.name