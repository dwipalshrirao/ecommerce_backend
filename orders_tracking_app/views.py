from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException, NotFound
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from utils.utility_functions import custom_response, CustomPagination
# from utils.model_constants import PurchaseOrderModelConstants

from utils.swagger_schemas import vender_get_list_api_swagger_kwargs


class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    http_method_names = ['get', 'post', 'head', 'delete','put']
    paginator= CustomPagination()

    def get_PurchaseOrder_object(self, purchase_order_id):
        try:
            return PurchaseOrder.objects.get(purchase_order_id = purchase_order_id)
        except PurchaseOrder.DoesNotExist:
            raise NotFound("PurchaseOrder not found.")
        

    @swagger_auto_schema(**vender_get_list_api_swagger_kwargs)
    def  list(self, request, *args, **kwargs):
        paginated_queryset = self.paginator.paginate_queryset(self.queryset, request)
        # serializer = PostsOfUserSerializer(page, many=True)
        serializer = self.serializer_class(paginated_queryset, many=True)
        response = self.paginator.get_paginated_response(serializer.data )
        return custom_response(response, is_pagination=True)
    
    
    @swagger_auto_schema()
    def destroy(self, request, *args, **kwargs):
        PurchaseOrder_object = self.get_PurchaseOrder_object(purchase_order_id=kwargs.get("pk"))
        PurchaseOrder_object.delete()
        return custom_response({}, message="record deleted", status= status.HTTP_404_NOT_FOUND)
    
    
    def create(self, request, *args, **kwargs):
        requested_data = request.data
        serializer = self.serializer_class(data=requested_data)
        if serializer.is_valid(raise_exception=True):
            PurchaseOrder_object = serializer.save()
            serializerd_PurchaseOrder_data = self.serializer_class(PurchaseOrder_object)
            return custom_response(serializerd_PurchaseOrder_data.data, message="PurchaseOrder created")


    def update(self, request, *args, **kwargs):
        requested_data = request.data
        PurchaseOrder_object = self.get_PurchaseOrder_object(purchase_order_id=kwargs["pk"])
        serializer = self.serializer_class(PurchaseOrder_object, data=requested_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            PurchaseOrder_object = serializer.save()
            serializerd_PurchaseOrder_data = self.serializer_class(PurchaseOrder_object)
            return custom_response(serializerd_PurchaseOrder_data.data, message="vendor details updated.")
        
        
    def retrieve(self, request, *args, **kwargs):
        PurchaseOrder_object = self.get_PurchaseOrder_object(purchase_order_id=kwargs["pk"])
        serializerd_PurchaseOrder_data = self.serializer_class(PurchaseOrder_object)
        return custom_response(serializerd_PurchaseOrder_data.data)
