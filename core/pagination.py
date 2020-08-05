import math
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param

from core.constants import FORMAT_CSV


class LinkHeaderPagination(pagination.PageNumberPagination):
    def get_last_link(self):
        total_count = self.page.paginator.count
        per_page_count = self.get_page_size(self.request)
        total_pages = int(math.ceil(float(total_count) / per_page_count))
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, total_pages)

    def get_page_size(self, request):
        kwargs = request.parser_context.get('kwargs')
        if kwargs and kwargs.get('format') == FORMAT_CSV:
            return None
        else:
            return self.page_size

    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        last_url = self.get_last_link()

        total_items = self.page.paginator.count
        item_starting_index = self.page.start_index() - 1
        item_ending_index = self.page.end_index() - 1

        content_range = '{0}-{1}/{2}'.format(item_starting_index, item_ending_index, total_items)

        links = []
        if next_url is not None:
            links.append('<{next_url}>; rel="next"'.format(next_url=next_url))
        if previous_url is not None:
            links.append('<{previous_url}>; rel="prev"'.format(previous_url=previous_url))
        links.append('<{last_url}>; rel="last"'.format(last_url=last_url))

        link_string = ', '.join(links)
        headers = {'Link': link_string, 'Content-Range': content_range} if link_string else {}

        return Response(data, headers=headers)