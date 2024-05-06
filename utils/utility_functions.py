import random
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .constants import PAGE_SIZE_QUERY_PARAM, PAGINATION_DEFAULT_PAGE_SIZE, PAGINATION_MAX_PAGE_SIZE





User = get_user_model()


def custom_response(data={}, message='response successfull', status = status.HTTP_200_OK,  is_pagination=False):
       if not is_pagination:
            return Response({'status_code': status, 'data': data, 'message': message}, status=status)
       return Response({'status_code': status, **data, 'message': message}, status=status)



class CustomPagination(PageNumberPagination):
    page_size = PAGINATION_DEFAULT_PAGE_SIZE
    page_size_query_param = PAGE_SIZE_QUERY_PARAM
    max_page_size = PAGINATION_MAX_PAGE_SIZE
    def get_paginated_response(self, data):
        return {
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'data': data,
        }




# def basic_permission(request, requested_user_uuid):
#     user = request.user
#     requested_user = None
#     try:
#         requested_user = User.objects.get(uuid=requested_user_uuid)
#     except:
#         raise NotFound(ERROR_USER_NOT_EXIST)
    
#     if user.uuid == requested_user.uuid:
#         if (user.user_type.user_type_name == USER_TYPE_NAME_ENTRY_ATHLETE) or (user.user_type.user_type_name == USER_TYPE_NAME_ENTRY_COACH):
#             return (True, requested_user)

#     elif user.user_type.user_type_name == USER_TYPE_NAME_ENTRY_GUARDIAN:
#         guardian_athlete = user.athlete_guardian_relation_guardian_user_id_model_manager.filter(
#                athlete_user_id=requested_user, athlete_guardian_relation_status_id__athlete_guardian_relation_status_type=ATHLETE_GUARDIAN_RELATION_STATUS_TYPE_ENTRY_ACCEPTED)
#         if guardian_athlete.exists():
#             return (True, requested_user)

#     return (False, requested_user)
