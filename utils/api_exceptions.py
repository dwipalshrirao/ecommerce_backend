from rest_framework.exceptions import APIException
from rest_framework import status

# from utils.success_error_messages.global_messages import ERROR_EMAIL_NOT_VERIFIED, ERROR_PHONE_NOT_VERIFIED, ERROR_USER_REGISTRATION_FAILED


# class RegistrationFailedException(APIException):
#     status_code = 500
#     default_detail = ERROR_USER_REGISTRATION_FAILED


# class PhoneNotVerifiedException(APIException):
#     status_code = status.HTTP_403_FORBIDDEN
#     default_detail = ERROR_PHONE_NOT_VERIFIED

#     def __init__(self, message=None, response_data={}):
#         super().__init__(detail=message)
#         self.response_data = response_data


# class EmailNotVerifiedException(APIException):
#     status_code = status.HTTP_403_FORBIDDEN
#     default_detail = ERROR_EMAIL_NOT_VERIFIED

#     def __init__(self, message=None, response_data={}):
#         super().__init__(detail=message)
#         self.response_data = response_data

