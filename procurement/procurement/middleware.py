from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect

URLS = [reverse(url) for url in settings.SUBSCRIPTION_REQUIRED_URL]

class CheckMembership():
	def process_request(self, request):
		if request.user.is_authenticated():
			#messages.success(request, 'user logged in')
			if request.path in URLS:
				role = request.user.userrole
				if str(role) == 'Regular':
					messages.error(request,'subscription required')
					return HttpResponseRedirect('/')
		else:
			messages.error(request,'you need to login')

'''
SELLER_URL = [reverse(url) for url in settings.SELLER_SPECIFIC_URL]
class IsSeller():
	def process_request(self, request):
			
		if request.path in SELLER_URL:
			user_type = request.user.usertype
			if str(user_type) == 'Consumer':
				messages.error(request,'Consumer can not Bid')
				return HttpResponseRedirect('/')'''
		

