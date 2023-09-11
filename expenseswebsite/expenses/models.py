from django.db import models

# Create your models here.
from django.utils.timezone import now
from django.contrib.auth.models import User
class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255,default='null')
        
    def __str__(self) -> str:
        return self.category
    
    class Meta:
        ordering = ["-date"]
        
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        
        verbose_name_plural = "Categories"
                
    def __str__(self):
        return self.name
    
    
        
    
    