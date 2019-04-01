from django.db import models

class Profile(models.Model):
	name = models.CharField(max_length=100)
	image= models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)

	def __str__(self):
		return self.name