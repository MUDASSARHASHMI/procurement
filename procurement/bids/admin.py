from django.contrib import admin
from .models import Bid
# Register your models here.
class BidAdmin(admin.ModelAdmin):
	list_display = ['user','order','bid_price','active']
	class Meta:
		model = Bid
admin.site.register(Bid, BidAdmin)
