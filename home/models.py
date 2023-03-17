from django.db import models
from django.contrib.auth.models import User


class PageConfig(models.Model):
	page_name = models.CharField(max_length = 50)
	title = models.CharField(max_length = 50,null=True,blank=True)
	meta_keywords = models.CharField(max_length = 300,null=True,blank=True)
	meta_author = models.CharField(max_length = 50,null=True,blank=True)
	meta_description = models.CharField(max_length=500,null=True,blank=True)
	calling_number = models.CharField(max_length = 50,null=True,blank=True)
	

	def __str__(self):
		return self.page_name
	
class Leads(models.Model):
	name = models.CharField(max_length = 50,null=True,blank=True)
	email = models.CharField(max_length = 50,null=True,blank=True)
	phone = models.CharField(max_length = 50)
	query = models.CharField(max_length = 200,null=True,blank=True)

	def __str__(self):
		return self.name
	

class Banners(models.Model):
	name = models.CharField(max_length = 50,null=True,blank=True)
	image = models.ImageField(upload_to='images')
	caption = models.CharField(max_length=100,null=True,blank=True)
	button_text = models.CharField(max_length=100,null=True,blank=True)
	page_name = models.CharField(max_length=50,default='index')
	button_link = models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.name
	
class Testimonials(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)
	message = models.CharField(max_length=200,null=True,blank=True)
	city = models.CharField(max_length=50,null=True,blank=True)
	image = models.ImageField(upload_to='testimonials',null=True,blank=True)

	def __str__(self):
		return self.name