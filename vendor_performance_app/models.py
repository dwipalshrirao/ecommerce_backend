from django.db import models
from utils.mixins import BaseModelMixin
# Create your models here.
from vendor_profile_app.models import Vendor


class vendorPerformanceHistory(BaseModelMixin):
    vendor_perf_id = models.AutoField(primary_key=True, db_column="vendor_perf_id")
    vendor_id = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField() # Historical record of the on-time delivery rate.
    quality_rating_avg = models.FloatField() #  Average rating of quality based on purchase orders.
    average_response_time = models.FloatField() #  Historical record of the average response time.
    fulfillment_rate = models.FloatField() #  Historical record of the fulfilment rate.



# ● vendor: ForeignKey - Link to the Vendor model.
# ● date: DateTimeField - Date of the performance record.
# ● on_time_delivery_rate: FloatField - Historical record of the on-time delivery rate.
# ● quality_rating_avg: FloatField - Historical record of the quality rating average.
# ● average_response_time: FloatField - Historical record of the average response
# time.
# ● fulfillment_rate: FloatField - Historical record of the fulfilment rate.