from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField()
	message = models.CharField(max_length=2000)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email