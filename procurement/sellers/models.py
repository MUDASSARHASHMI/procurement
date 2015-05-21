from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SellerCompany(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	about = models.CharField(max_length=1500, blank=True, null=True)
	company_type = models.CharField(max_length=120, help_text='public or private?')
	gst_number = models.CharField(max_length=120)
	date_joined =  models.DateTimeField(auto_now_add=True,auto_now=False)
	date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "companies"




class SellerAddress(models.Model):
	user = models.ForeignKey(User)
	company = models.ForeignKey(SellerCompany)
	street_address = models.CharField(max_length=150)
	city = models.CharField(max_length=150)
	zipcode = models.IntegerField(max_length=5,blank=True, null=True)

	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	active = models.BooleanField(default=True)
	

	def __unicode__(self):
		return self.city

	class Meta:
		verbose_name_plural = "Addresses"
