from api import API

# def app(environ, start_response):
#     response_body = b"Hello, World!"
#     status = "200 OK"
#     start_response(status, headers=[])
#     return iter([response_body])

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"

# @app.route("/home")
# def home2(request, response):
#     response.text = "Hello from the SECOND HOME page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/book")
class BooksHandler:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"