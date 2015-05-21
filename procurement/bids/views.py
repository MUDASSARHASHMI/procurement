from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from customers.models import UserType

from .forms import BidForm
# Create your views here.


def bid(request, order_slug):
	if UserType.objects.is_seller(request.user):
		form = BidForm(request.POST or None)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.user = request.user
			new_form.order.slug = order_slug
			new_form.save()
		return render_to_response('bids/bid.html', locals(), context_instance=RequestContext(request))
	else:
		messages.error(request, 'consumer account can not bid')
		return HttpResponseRedirect('/')


		
