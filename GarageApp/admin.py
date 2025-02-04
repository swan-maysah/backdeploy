from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')


@admin.register(Taskform)
class TaskformAdmin(admin.ModelAdmin):
    list_display = ('customer', 'car_plate_number', 'service_type', 'description', 'cost', 'task_date') 

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Taskform', 'status', 'amount_paid', 'payment_method', 'processed_at') 
  
      