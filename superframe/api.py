# api.py
from parse import parse
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
            print(path)
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response, *args, **kwargs):
        request = Request(environ)

        # response = Response()
        # response.text = "hello, from superfarme"
        response = self.handle_request(request)

        return response(environ,start_response)


    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None


    def handle_request(self, request):
        # user_agent = request.environ.get("HTTP_USER_AGENT", "No user agent found")
        print(request.path)

        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        # if request.path == "/favicon.ico":
        #     return response
        if handler:
            handler(request,response,**kwargs)

        else:
            self.default_response(response)

        # for path, handler in  self.routes.items():
        #     print(path,handler)
        #     if path == request.path:
        #         handler(request,response)
        return response

        # response.text = f"Hello, message carried by {user_agent}"

        # return response