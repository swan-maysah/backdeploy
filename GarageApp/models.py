from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Taskform(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='tasks')
    car_plate_number = models.CharField(max_length=15)
    SERVICE_TYPE_CHOICES = [
        ('Service', 'Service'),
        ('Repairs', 'Repairs'),
    ]
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    task_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name}-{self.car_plate_number}"

    #payment 
class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    ]
    Taskform = models.OneToOneField(Taskform, on_delete=models.CASCADE, related_name='payment')
    status = models.CharField(max_length=10,choices=PAYMENT_STATUS_CHOICES,default='pending')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for{self.Taskform.car_plate_number}"