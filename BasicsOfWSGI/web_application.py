from wsgiref.simple_server import make_server


def application(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/':
        response_body = "Index"
    else:
        response_body = "Hello"
    status = "200 OK"
    response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return [bytes(response_body,'utf-8')]

# httpd = make_server(
#     '127.0.0.1', 8051, application)

# httpd.serve_forever()

# run with gunicorn "gunicorn web_application:application --bind=localhost:8051"
# run with uwsgi "uwsgi --http :8051 --wsgi-file web_application.py"
# kill the process: "sudo fuser -k 8051/tcp"
