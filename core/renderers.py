from collections import OrderedDict

from inflection import camelize
from rest_framework.renderers import JSONRenderer


def camelize_response(data):
    if isinstance(data, dict):
        return OrderedDict((camelize(key, False), camelize_response(value)) for key, value in list(data.items()))

    if isinstance(data, list):
        return [camelize_response(x) for x in data]

    if isinstance(data, tuple):
        return tuple(camelize_response(x) for x in data)

    return data


class CamelCaseJSONRenderer(JSONRenderer):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(camelize_response(data), *args, **kwargs)