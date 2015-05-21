from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
import stripe
from procurement.stripe_info import secret_key


stripe.api_key = secret_key

# Create your models here.

class UserTypeManager(models.Manager):
	def is_seller(self, user):
		return super(UserTypeManager, self).filter(user=user).filter(user_type__startswith='Sell')

CHOICES = (
	('Seller','Seller'),
	('Consumer','Consumer'),
	)
class UserType(models.Model):
	user = models.OneToOneField(User)
	user_type = models.CharField(max_length=120, default='', choices=CHOICES)

	objects = UserTypeManager()

	def __unicode__(self):
		return self.user.username


CHOICES = (
	('Regular','Regular'),
	('Staff','Staff'),
	('Premium','Premium'),
	)
class UserRole(models.Model):
	user = models.OneToOneField(User)
	role = models.CharField(max_length=120, default='Regular', choices=CHOICES)

	def __unicode__(self):
		return self.user.username


class UserStripe(models.Model):
	user = models.OneToOneField(User)
	stripe_id = models.CharField(max_length=120)

	def __unicode__(self):
		return self.user.username

	def get_stripe_id(self):
		return self.stripe_id


def CreateStripeId(sender, user, request, **kwargs):
	new_id, created = UserStripe.objects.get_or_create(user=user)
	if created:
		print created
		stripe_cust = stripe.Customer.create(email=user.email, description='Customer for %s' %user.email)
		print stripe_cust.id
		new_id.stripe_id = stripe_cust.id
		new_id.save() 
	else:
		print 'not created'

user_logged_in.connect(CreateStripeId)