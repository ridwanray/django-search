from django.db import models

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=15, unique=True,  null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False,  null=True)	
	
	class Meta:
	  verbose_name_plural = "Categories"
	  
	def __str__(self):
		return self.title
						
						
class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	category = models.ForeignKey('Category', blank=True, on_delete=models.CASCADE, null=True)					
	

	def __str__(self):
		return self.name