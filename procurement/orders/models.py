from django.db import models
from django.contrib.auth.models import User
from consumers.models import ConsumerCompany
# Create your models here.


class Order(models.Model):
	user = models.ForeignKey(User)
	company = models.ForeignKey(ConsumerCompany)
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	description = models.CharField(max_length=2000,blank=False, null=False)
	pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	expire_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.title

