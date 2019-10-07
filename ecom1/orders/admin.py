from django.contrib import admin
from .models import  staff_contractor_company,assset_tracker_activity,Location,history_order





# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'contact_number', 'city', 'paid', 'created',
#                     'updated']
#     list_filter = ['paid', 'created', 'updated']
 


# admin.site.register(Order, OrderAdmin)
admin.site.register(staff_contractor_company)
admin.site.register(assset_tracker_activity)
admin.site.register(Location)
admin.site.register(history_order)