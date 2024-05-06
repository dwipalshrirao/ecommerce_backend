from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
import uuid

from utils.mixins import BaseModelMixin

User = get_user_model()



class Vendor(BaseModelMixin):
    vendor_id = models.AutoField(primary_key=True, db_column="vendor_id")
    name = models.CharField(max_length=100)
    contact_details = models.TextField() # Contact information of the vendor.
    address = models.TextField()  # Contact information of the vendor.
    vendor_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False) # A unique identifier for the vendor.
    on_time_delivery_rate = models.FloatField(null=True, blank=True) # Tracks the percentage of on-time deliveries.
    quality_rating_avg = models.FloatField(null=True, blank=True) #  Average rating of quality based on purchase orders.
    average_response_time = models.FloatField(null=True, blank=True) #  Average time taken to acknowledge purchase orders.
    fulfillment_rate = models.FloatField(null=True, blank=True) #  Percentage of purchase orders fulfilled successfully.

    def change_vendor_code(self):
        self.vendor_code = uuid.uuid4()
        return self.vendor_code
    
    def __str__(self):
        return f"vendor id - {self.vendor_id} | vendor code - {self.vendor_code}"

# name: CharField - Vendor's name.
# ● contact_details: TextField - Contact information of the vendor.
# ● address: TextField - Physical address of the vendor.
# ● vendor_code: CharField - A unique identifier for the vendor.
# ● on_time_delivery_rate: FloatField - Tracks the percentage of on-time deliveries.
# ● quality_rating_avg: FloatField - Average rating of quality based on purchase
# orders.
# ● average_response_time: FloatField - Average time taken to acknowledge
# purchase orders.
# ● fulfillment_rate: FloatField - Percentage of purchase orders fulfilled successfully.