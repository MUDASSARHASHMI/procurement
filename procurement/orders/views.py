from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Order
# Create your views here.

def all_orders(request):

	all_orders = Order.objects.all()
	return render_to_response("orders/all_orders.html", locals(), context_instance=RequestContext(request))

def view_order(request, slug):
	order = Order.objects.get(slug=slug)
	return render_to_response('orders/view_order.html', locals(), RequestContext(request))