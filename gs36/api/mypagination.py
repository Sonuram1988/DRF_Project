from rest_framework.pagination import PageNumberPagination

class myPageNumberSize(PageNumberPagination):
    page_size=5
    page_query_param='myPage'
    page_size_query_param='records'
    max_page_size=7
    last_page_strings='end'