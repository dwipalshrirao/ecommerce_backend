
from dataclasses import fields
from random import random
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import PurchaseOrder
from utils.model_constants import purchanseOrderModelConstants, BaseModelConstants


User = get_user_model()


class PurchaseOrderSerializer(serializers.ModelSerializer):
    po_number = serializers.UUIDField( read_only=True)
    creation_date = serializers.DateTimeField( read_only=True)
    modification_date = serializers.DateTimeField( read_only=True)
    

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderSerializer, self).__init__(*args, **kwargs) # call the super() 
        for field in self.fields: # iterate over the serializer fields
            # print(self.fields, self)
            self.fields[field].error_messages['required'] = '%s field is required'%field # set the custom error message

    # def validate(self, attrs):
    #     status = attrs[purchanseOrderModelConstants.status_field]

    #     if status.lower() not in [purchanseOrderModelConstants.order_status_value_cancelled,
    #                               purchanseOrderModelConstants.order_status_value_completed,
    #                               purchanseOrderModelConstants.order_status_value_pending]:
    #         raise serializers.ValidationError(f"only given status are allowed - '{purchanseOrderModelConstants.order_status_value_cancelled}',\
    #                               '{purchanseOrderModelConstants.order_status_value_completed}', \
    #                               '{purchanseOrderModelConstants.order_status_value_pending}'") 
    #     return super().validate(attrs)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        
 

