from django.contrib import admin
from .models import Order

# Register your models here.




class OrderAdmin(admin.ModelAdmin):
	list_display = ['user','title', 'slug','pub_date']
	readonly_fields = ['timestamp','updated']
	prepopulated_fields = {"slug": ("title",)}
	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)


