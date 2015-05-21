import datetime
from django.shortcuts import render, render_to_response, RequestContext, Http404
from customers.models import UserRole
from .forms import UserTypeForm
import stripe
from procurement.stripe_info import secret_key, publishable_key

stripe.api_key = secret_key
# Create your views here.

def get_stripe_customer(user):
	try:
		stripe_id = user.userstripe.stripe_id

	except:
		stripe_id = False
	if stripe_id:
		customer = stripe.Customer.retrieve(stripe_id)
		return customer
	else:
		pass

def subscribe(request):
	if request.user.is_authenticated():
		#subscription chocie
		#assign that choice after successful payments
		#collect credit cards here
		pub_key = publishable_key
		customer = get_stripe_customer(request.user)
		

		if request.method == 'POST':
			print request.POST
			membership = request.POST['membership']
			token = request.POST['stripeToken']
			customer.cards.create(card=token)
			customer.subscriptions.create(plan=membership)
			customer.save()

		return render_to_response('customers/subscribe.html', locals(),context_instance=RequestContext(request))
	else:
		return render_to_response('orders/all_orders.html', locals(),context_instance=RequestContext(request))


'''def add_company_details(request):
	if request.user.is_authenticated():
		form = CompanyForm(request.POST or None)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.user = request.user
			new_form.date_joined = datetime.datetime.now()
			new_form.save()
		return render_to_response("customers/add_company_details.html", locals(), RequestContext(request)) '''


def account_type(request):
	if request.user.is_authenticated():
		form = UserTypeForm(request.POST or None)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.user = request.user
			new_form.save()
		return render_to_response("customers/account_type.html", locals(), RequestContext(request)) 
	else:
		raise Http404
