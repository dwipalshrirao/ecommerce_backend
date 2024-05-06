from django.utils import timezone

from utils.model_constants import purchanseOrderModelConstants, vendorModelConstants

from vendor_performance_app.models import vendorPerformanceHistory
from orders_tracking_app import models


def handle_purchase_order_completed(sender, instance, **kwargs):

    if getattr(instance, purchanseOrderModelConstants.status_field) == purchanseOrderModelConstants.order_status_value_completed:
        vendor_obj = getattr(instance, purchanseOrderModelConstants.vendor_id_field)

        historical_on_time_delivery_rate = getattr(vendor_obj, vendorModelConstants.on_time_delivery_rate_field)
        # historical_quality_rating_avg = getattr(vendor_obj, vendorModelConstants.quality_rating_avg_field)
        historical_average_response_time = getattr(vendor_obj, vendorModelConstants.average_response_time_field)
        historical_fulfillment_rate = getattr(vendor_obj, vendorModelConstants.fulfillment_rate_field)

        #calulate quality rating
        quality_rating_filter = {purchanseOrderModelConstants.status_field : purchanseOrderModelConstants.order_status_value_completed,
                  f"{purchanseOrderModelConstants.quality_rating_field}__isnull" : False}
        purchase_ordr_queryset = models.PurchaseOrder.objects.filter(**quality_rating_filter)

        if purchase_ordr_queryset:
            quality_ratings = [rating.quality_rating for rating in purchase_ordr_queryset]

            avg_quality_rating = sum(quality_ratings)/len(quality_ratings)
            # update vendor
            setattr(vendor_obj, vendorModelConstants.quality_rating_avg_field, avg_quality_rating)
            vendor_obj.save()
        
            vendor_performance_history_obj = vendorPerformanceHistory(
                    vendor_id = vendor_obj,
                    date = timezone.now(),
                    average_response_time = historical_average_response_time,
                    on_time_delivery_rate = historical_on_time_delivery_rate,
                    quality_rating_avg = avg_quality_rating,
                    fulfillment_rate = historical_fulfillment_rate
            )
            vendor_performance_history_obj.save()


def handle_acknowledgment_date_update(sender, instance, **kwargs):
    # print(instance, instance.purchase_order_id)
    po_id = getattr(instance, purchanseOrderModelConstants.purchase_order_id_field)
    if not po_id:
        return
    
    po_obj = models.PurchaseOrder.objects.get(**{
                            purchanseOrderModelConstants.purchase_order_id_field: po_id
                            })
    prev_achknowledged_date = getattr(po_obj, purchanseOrderModelConstants.acknowledgment_date_field)
    # new_achknowledged_date = getattr(instance, purchanseOrderModelConstants.acknowledgment_date_field)

    if prev_achknowledged_date is not None:
        return
    
    po_queryset_of_vendor_filter = {
                purchanseOrderModelConstants.vendor_id_field: getattr(po_obj, 
                                                                        purchanseOrderModelConstants.vendor_id_field),
                f"{purchanseOrderModelConstants.issue_date_field}__isnull" : False,
                f"{purchanseOrderModelConstants.acknowledgment_date_field}__isnull" : False,
                }
    po_queryset_of_vendor = models.PurchaseOrder.objects.filter(**po_queryset_of_vendor_filter)
    if not po_queryset_of_vendor:
        return
    
    # calculate average_response_time
    diffrence_in_hours = []
    for po_item in po_queryset_of_vendor:
        print(getattr(po_item, purchanseOrderModelConstants.acknowledgment_date_field), 
                getattr(po_item, purchanseOrderModelConstants.issue_date_field))
        aknowledge_date = getattr(po_item, purchanseOrderModelConstants.acknowledgment_date_field) 
        issue_date = getattr(po_item, purchanseOrderModelConstants.issue_date_field)
        diff = (aknowledge_date - issue_date).total_seconds() / (60 * 60)
        diffrence_in_hours.append(round(diff))

    average_response_time = sum(diffrence_in_hours) / len(diffrence_in_hours)


    vendor_obj = getattr(po_obj, purchanseOrderModelConstants.vendor_id_field)

    historical_on_time_delivery_rate = getattr(vendor_obj, vendorModelConstants.on_time_delivery_rate_field)
    historical_quality_rating_avg = getattr(vendor_obj, vendorModelConstants.quality_rating_avg_field)
    historical_fulfillment_rate = getattr(vendor_obj, vendorModelConstants.fulfillment_rate_field)

    # update vendor
    setattr(vendor_obj, vendorModelConstants.average_response_time_field, average_response_time)
    vendor_obj.save()

    vendor_performance_history_obj = vendorPerformanceHistory(
            vendor_id = vendor_obj,
            date = timezone.now(),
            average_response_time = average_response_time,
            on_time_delivery_rate = historical_on_time_delivery_rate,
            quality_rating_avg = historical_quality_rating_avg,
            fulfillment_rate = historical_fulfillment_rate
    )
    vendor_performance_history_obj.save()

    # pass