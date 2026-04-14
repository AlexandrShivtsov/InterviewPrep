from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
import math


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50
    
    def get_paginated_response(self, data):
        # Get tech from view context
        tech = self.request.parser_context.get('view').get_serializer_context().get('tech', 'Unknown')
        
        # Calculate total pages
        total_pages = math.ceil(self.count / self.limit) if self.count > 0 else 1
        
        return Response({
            'response': {
                'tech': tech,
                'previous': self.get_previous_link(),
                'next': self.get_next_link(),
                'total_pages': total_pages,
                'total_items': self.count,
            },
            'data': data
        })
        

class QuizPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
    
    def get_paginated_response(self, data):
        # Get tech from view context
        tech = self.request.parser_context.get('view').get_serializer_context().get('tech', 'Unknown')
        
        return Response({
            'response': {
                'tech': tech,
                'previous': self.get_previous_link(),
                'next': self.get_next_link(),
                'total_pages': self.page.paginator.num_pages,
                'total_items': self.page.paginator.count,
            },
            'data': data
        })