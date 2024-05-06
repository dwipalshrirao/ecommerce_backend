
from dataclasses import fields
from random import random
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Vendor
from utils.model_constants import vendorModelConstants


User = get_user_model()


class VendorSerializer(serializers.ModelSerializer):
    vendor_code = serializers.UUIDField( read_only=True)
    creation_date = serializers.DateTimeField( read_only=True)
    modification_date = serializers.DateTimeField( read_only=True)

    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs) # call the super() 
        for field in self.fields: # iterate over the serializer fields
            print(self.fields, self)
            self.fields[field].error_messages['required'] = '%s field is required'%field # set the custom error message
    



    class Meta:
        model = Vendor
        fields = '__all__'
        # read_only_fields = (vendorModelConstants.vendor_id_field,
        #                     vendorModelConstants.vendor_code_field)
        
 

