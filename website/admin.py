from django.contrib import admin
from .models import Appointment,Contact
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['your_name','schedule_dates','schedule_days','your_messagess','time_stamp']    
admin.site.register(Appointment,AppointmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['your_name', 'your_mail','your_messagess']
admin.site.register(Contact,ContactAdmin)
