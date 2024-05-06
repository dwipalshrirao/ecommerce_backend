
from urllib import request
from rest_framework.views import exception_handler
from utils.constants import *



def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        
        if isinstance(response.data, dict):
            response.data[RESPONSE_KEY_MESSAGE] = response.data.get(
                RESPONSE_KEY_MESSAGE,  response.data.pop(RESPONSE_KEY_DETAIL, ""))
            if not response.data.get(RESPONSE_KEY_MESSAGE):
                errors = response.data
                response.data = {}
                for _, value in errors.items():
                    try:
                        response.data[RESPONSE_KEY_MESSAGE] = value[0]
                    except Exception as e:
                        response.data[RESPONSE_KEY_MESSAGE] = e
                    break
        
            response.data[RESPONSE_KEY_DATA] = response.data.get(RESPONSE_KEY_DATA, getattr(exc, RESPONSE_KEY_RESPONSE_DATA, {}) )
        elif isinstance(response.data, list):
            errors = response.data
            response.data = {}
            for error_message in errors:
                response.data[RESPONSE_KEY_MESSAGE] = error_message
                break
                
            response.data[RESPONSE_KEY_DATA] = getattr(exc, RESPONSE_KEY_RESPONSE_DATA, {})
        response.data[RESPONSE_KEY_STATUS_CODE] = response.status_code

    return response
