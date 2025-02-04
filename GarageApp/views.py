from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import customer, Taskform, Payment
from .serializers import customerSerializer, TaskformSerializer, PaymentSerializer

# Create your views here.
class customerViewSet(ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerSerializer

class TaskformViewSet(ModelViewSet):
    queryset = Taskform.objects.all()
    serializer_class = TaskformSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
