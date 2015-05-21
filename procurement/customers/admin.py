from django.contrib import admin
from .models import UserRole, UserStripe, UserType
# Register your models here.



class UserRoleAdmin(admin.ModelAdmin):
	list_display = ['user','role']
	class Meta:
		model = UserRole


admin.site.register(UserRole, UserRoleAdmin)



class UserStripeAdmin(admin.ModelAdmin):
	list_display = ['user']
	class Meta:
		model = UserStripe


admin.site.register(UserStripe, UserStripeAdmin)



class UserTypeAdmin(admin.ModelAdmin):
	list_display = ['user','user_type']
	class Meta:
		model = UserType


admin.site.register(UserType, UserTypeAdmin)

