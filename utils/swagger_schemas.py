from drf_yasg import openapi
from .constants import PAGE_SIZE_QUERY_PARAM, PAGINATION_DEFAULT_PAGE_SIZE

operation_description_key = 'operation_description'
responses_key = 'responses'
manual_parameters_key = 'manual_parameters'
tags_key = 'tags'

vender_get_list_api_swagger_kwargs = {
    # operation_description_key: """We can make any request to Elastic server using this API.
    #                             <b>Request Body</b>
    #                             {
    #                             "url": <URL + endpoint>, //required
    #                             "method": "<GET/POST/DELETE>" //required,
    #                             "requestBody": <Request body in Json format>
    #                             }
    #                             <b>Ex:-</b>
    #                             {
    #                                 "url": "http://139.162.210.220:9201/gg/_mappings",
    #                                 "method" : "GET",
    #                                 "requestBody": {}
    #                             }
    #                             """,
    manual_parameters_key: [
        # openapi.Parameter('token', openapi.IN_HEADER,
        #                                    description="You can get this token after signIn",
        #                                     type=openapi.IN_HEADER),
        openapi.Parameter(PAGE_SIZE_QUERY_PARAM, openapi.IN_QUERY,
                             description=f"number of records per page, default page_size - {PAGINATION_DEFAULT_PAGE_SIZE}",
                             type=openapi.TYPE_STRING),
                        #    openapi.Parameter('Authorization', openapi.IN_HEADER,
                        #                      description="""This is Basic Authorization token of elastic server.
                        #                                     If it authenticated then you can pass Basic Authorization token here
                        #                                     Basic <base64 encrypted username and password of elastic server>
                        #                                     ex:-
                        #                                     Basic ZWxhc3RpYzoyazIwMTAyMl9NQ1BM
                        #                                     """,
                        #                      type=openapi.IN_HEADER)
                                            
                                            ],
    # tags_key: ["Elasticsearch API"],
    # responses_key: {
    #     200: """""",
    # }
}





purchase_order_get_list_api_swagger_kwargs = {

    manual_parameters_key: [
        # openapi.Parameter('token', openapi.IN_HEADER,
        #                                    description="You can get this token after signIn",
        #                                     type=openapi.IN_HEADER),
        openapi.Parameter(PAGE_SIZE_QUERY_PARAM, openapi.IN_QUERY,
                             description=f"number of records per page, default page_size - {PAGINATION_DEFAULT_PAGE_SIZE}",
                             type=openapi.TYPE_STRING),
                        #    openapi.Parameter('Authorization', openapi.IN_HEADER,
                        #                      description="""This is Basic Authorization token of elastic server.
                        #                                     If it authenticated then you can pass Basic Authorization token here
                        #                                     Basic <base64 encrypted username and password of elastic server>
                        #                                     ex:-
                        #                                     Basic ZWxhc3RpYzoyazIwMTAyMl9NQ1BM
                        #                                     """,
                        #                      type=openapi.IN_HEADER)
                                            
                                            ],
}