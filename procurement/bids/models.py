from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
from sellers.models import SellerCompany
# Create your models here.
class Bid(models.Model):
	user = models.ForeignKey(User)
	order = models.ForeignKey(Order)
	company = models.ForeignKey(SellerCompany)
	bid_price = models.DecimalField(max_digits=10, decimal_places=2)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.user.username

	class Meta:
		ordering = ['-timestamp']

