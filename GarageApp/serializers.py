from rest_framework import serializers
from . models import *


class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class TaskformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskform
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'