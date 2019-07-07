# api.py
from webob import Request, Response
class API:

    # def __call__(self, environ, start_response, *args, **kwargs):
    #     response_body = b"Hello, World!"
    #     status = "200 OK"
    #     start_response(status,headers=[])
    #     return iter([response_body])

    def __init__(self):
        self.routes = {}

    def route(self,path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response, *args, **kwargs):
        request = Request(environ)

        # response = Response()
        # response.text = "hello, from superfarme"
        response = self.handle_request(request)

        return response(environ,start_response)

    def handle_request(self, request):
        # user_agent = request.environ.get("HTTP_USER_AGENT", "No user agent found")
        print(request.path)

        response = Response()

        for path, handler in  self.routes.items():
            if path == request.path:
                handler(request,response)
                return response

        # response.text = f"Hello, message carried by {user_agent}"

        # return response