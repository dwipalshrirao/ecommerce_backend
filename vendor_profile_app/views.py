from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException, NotFound
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Vendor
from .serializers import VendorSerializer
from utils.utility_functions import custom_response, CustomPagination
from utils.model_constants import vendorModelConstants

from utils.swagger_schemas import vender_get_list_api_swagger_kwargs


class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    http_method_names = ['get', 'post', 'head', 'delete','put']
    paginator= CustomPagination()

    def get_vendor_object(self, vendor_id):
        try:
            return Vendor.objects.get(vendor_id = vendor_id)
        except Vendor.DoesNotExist:
            raise NotFound("vendor not found.")
        

    @swagger_auto_schema(**vender_get_list_api_swagger_kwargs)
    def  list(self, request, *args, **kwargs):
        paginated_queryset = self.paginator.paginate_queryset(self.queryset, request)
        # serializer = PostsOfUserSerializer(page, many=True)
        serializer = self.serializer_class(paginated_queryset, many=True)
        response = self.paginator.get_paginated_response(serializer.data )
        return custom_response(response, is_pagination=True)
    
    
    def destroy(self, request, *args, **kwargs):
        vendor_object = self.get_vendor_object(vendor_id=kwargs.get("pk"))
        vendor_object.delete()
        return custom_response({}, message="record deleted", status= status.HTTP_404_NOT_FOUND)
    
    
    def create(self, request, *args, **kwargs):
        requested_data = request.data
        serializer = self.serializer_class(data=requested_data)
        if serializer.is_valid(raise_exception=True):
            vendor_object = serializer.save()
            serializerd_vendor_data = self.serializer_class(vendor_object)
            return custom_response(serializerd_vendor_data.data, message="vendor created")


    def update(self, request, *args, **kwargs):
        requested_data = request.data
        vendor_object = self.get_vendor_object(vendor_id=kwargs["pk"])
        serializer = self.serializer_class(vendor_object, data=requested_data)
        if serializer.is_valid(raise_exception=True):
            vendor_object = serializer.save()
            serializerd_vendor_data = self.serializer_class(vendor_object)
            return custom_response(serializerd_vendor_data.data, message="vendor details updated.")
        
        
    def  retrieve(self, request, *args, **kwargs):
        vendor_object = self.get_vendor_object(vendor_id=kwargs["pk"])
        serializerd_vendor_data = self.serializer_class(vendor_object)
        return custom_response(serializerd_vendor_data.data)
