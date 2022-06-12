from django.db import models

# Create your models here.


class Customer(models.Model):
	full_name = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        phone_number = models.CharField(max_length=200)
	date_of_birth = models.CharField(max_length=200)

	def __str__(self):
		return self.full_name 
 
