from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param="myLimit"
    offset_query_param='myOffset'
    max_limit=7