from typing import Iterable
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
import uuid

from vendor_profile_app.models import Vendor
from utils.mixins import BaseModelMixin
from orders_tracking_app.signals import handle_purchase_order_completed, handle_acknowledgment_date_update

from utils.model_constants import purchanseOrderModelConstants

User = get_user_model()



class PurchaseOrder(BaseModelMixin):

    status_choices = [
        (purchanseOrderModelConstants.order_status_value_pending,purchanseOrderModelConstants.order_status_value_pending),
          (purchanseOrderModelConstants.order_status_value_completed, purchanseOrderModelConstants.order_status_value_completed),
          (purchanseOrderModelConstants.order_status_value_cancelled, purchanseOrderModelConstants.order_status_value_cancelled)
    ]
    purchase_order_id = models.AutoField(primary_key=True, db_column="purchase_order_id")
    po_number = models.UUIDField(default=uuid.uuid4, unique=True, editable=False) # Unique number identifying the PO.
    vendor_id = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING, db_column="vendor_id") # Link to the Vendor model.
    order_date = models.DateTimeField(auto_now_add=True, editable=False) # Date when the order was placed.
    delivery_date = models.DateTimeField(null=True, blank=True) # Expected or actual delivery date of the order.
    items = models.JSONField() # Details of items ordered.
    quantity = models.IntegerField() # Total quantity of items in the PO.
    status = models.CharField(choices=status_choices, max_length=10) # Current status of the PO (e.g., pending, completed, canceled).
    quality_rating = models.FloatField(null=True, blank=True) # Rating given to the vendor for this PO (nullable).
    issue_date =  models.DateTimeField() # Timestamp when the PO was issued to the vendor.
    acknowledgment_date =  models.DateTimeField(null=True, blank=True) # Timestamp when the vendor acknowledged the PO.

    
    # def save(self, *args, **kwargs):
    #     print(args, kwargs)
    #     print(self)
 
    #     # call the parent's save() method
    #     super(PurchaseOrder, self).save(*args, **kwargs)
    
    def change_po_number(self):
        self.po_number = uuid.uuid4()
        return self.po_number
    
    def __str__(self):
        return f"vendor id - {self.vendor_id} | po_number - {self.po_number}"


models.signals.post_save.connect(handle_purchase_order_completed, sender=PurchaseOrder)
models.signals.pre_save.connect(handle_acknowledgment_date_update, sender=PurchaseOrder)

# po_number: CharField - Unique number identifying the PO.
# ● vendor: ForeignKey - Link to the Vendor model.
# ● order_date: DateTimeField - Date when the order was placed.
# ● delivery_date: DateTimeField - Expected or actual delivery date of the order.
# ● items: JSONField - Details of items ordered.
# ● quantity: IntegerField - Total quantity of items in the PO.
# ● status: CharField - Current status of the PO (e.g., pending, completed, canceled).
# ● quality_rating: FloatField - Rating given to the vendor for this PO (nullable).
# ● issue_date: DateTimeField - Timestamp when the PO was issued to the vendor.
# ● acknowledgment_date: DateTimeField, nullable - Timestamp when the vendor
# acknowledged the PO.
