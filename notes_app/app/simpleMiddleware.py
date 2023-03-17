from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import requests


class SimpleMiddleware(MiddlewareMixin):

    def _init_(self, get_response):
        self.get_response = get_response

    print("before call")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("after call 1")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        print("after call 2")

        URL = 'https://dummyjson.com/products/1'
        data = requests.get(URL)
        print(data.json())
        return response

    # nothing prints after here

