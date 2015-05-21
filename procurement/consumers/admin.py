from django.contrib import admin
from .models import ConsumerCompany, ConsumerAddress
# Register your models here.

class ConsumerCompanyAdmin(admin.ModelAdmin):
	list_display = ['user','name', 'date_joined']
	readonly_fields = ['date_joined','date_updated']
	class Meta:
		model = ConsumerCompany


admin.site.register(ConsumerCompany, ConsumerCompanyAdmin)




class ConsumerAddressAdmin(admin.ModelAdmin):
	list_display = ['user','city', 'active']
	readonly_fields = ['timestamp','updated']
	class Meta:
		model = ConsumerAddress

admin.site.register(ConsumerAddress, ConsumerAddressAdmin)

