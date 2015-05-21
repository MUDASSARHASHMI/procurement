from django.contrib import admin
from .models import SellerAddress, SellerCompany
# Register your models here.

class SellerCompanyAdmin(admin.ModelAdmin):
	list_display = ['user','name', 'date_joined']
	readonly_fields = ['date_joined','date_updated']
	class Meta:
		model = SellerCompany


admin.site.register(SellerCompany, SellerCompanyAdmin)


class SellerAddressAdmin(admin.ModelAdmin):
	list_display = ['user','city', 'active']
	readonly_fields = ['timestamp','updated']
	class Meta:
		model = SellerAddress

admin.site.register(SellerAddress, SellerAddressAdmin)

