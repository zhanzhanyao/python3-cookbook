def learn_urllib():
    """interact with http services as client"""
    from urllib import request, parse

    # Base URL being accessed
    url = "http://httpbin.org/get"
    # Dictionary of quary parameters (if any)
    parms = {
        "name1": "value1",
        "name2": "value2",
    }
    # Encode the quary string
    quarystring = parse.urlencode(parms)

    # Make a GET request and read response
    u = request.urlopen(url + "?" + quarystring)
    resp = u.read()

    # Make a post request and read the response
    u = request.urlopen(url, quarystring.encode("ascii"))

    # provide custom http header by request
    # Extra headers
    header = {
        "User-agent": "none/ofyourbusiness",
        "spam": "Eggs",
    }
    req = request.Request(url, quarystring.encode("ascii"), headers=header)

    # Make a request and read thee response
    u = request.urlopen(req)
    resp = u.read()


def learn_requests():
    # implement above functions using request module
    import requests

    # Base url being accessed
    url = "http://httpbin.org/post"
    # Dictionary of query parametor
    parms = {
        "name1": "value1",
        "name2": "value2",
    }
    # Extra header
    headers = {"User-agent": "none/ofyourbusiness", "Spam": "Eggs"}

    resp = requests.post(url, data=parms, headers=headers)
    # Decoded text returned by the request
    text = resp.text
    rjson = resp.json

    # make a HEAD request by requests module and get some http header
    import requests

    resp = requests.head("http://www.python.org/index.html")
    status = resp.status_code
    last_modified = resp.headers["last-modified"]
    content_type = resp.headers["content-type"]
    content_length = resp.headers["content-length"]

    # log in Pypi by authenticate using requests module
    import requests

    resp = requests.get(
        "http://pypi.python.org/pypi?:action=login", auth=("username", "password")
    )

    # Pass HTTP cookies from one request to another using requests module
    import requests

    url = "http://pypi.python.org/pypi?:action=login"
    # first requests
    resp1 = requests.get(url)
    # second requests with cookies received on first requests
    resp2 = requests.get(url, cookies=resp1.cookies)

    # upload by requests modules
    import requests

    url = "http://pypi.python.org/pypi?:action=login"
    files = {"files": ("data.csv", open("data.csv", "rb"))}

    r = requests.post(url, files=files)

    import requests

    r = requests.get("http://httpbin.org/get?name=Dave&n=37")
    resp = r.json()
    print(resp)


# def learn_tcp():
# Implement a server that comunite with client by the TCP protocol.
# skip


def learn_rest():
    """creating simple rest based interface"""
    import cgi

    def notfound_404(environ, start_response):
        start_response("404 Not Found", [("Content-type", "text/plain")])
        return [b"Not Found"]

    class PathDispatcher:
        def __init__(self):
            self.pathmap = {}

        def call(self, environ, start_response):
            path = environ["PATH_INFO"]
            params = cgi.FieldStorage(environ["wsgi.input"], environ=environ)
            method = environ["REQUEST_METHOD"].lower()
            environ["params"] = {key: params.getvalue(key) for key in params}
            handler = self.pathmap.get((method, path), notfound_404)
            return handler(environ, start_response)

        def register(self, method, path, function):
            self.pathmap[method.lower(), path] = function
            return function

    import time

    _hello_resp = """\
    <html>
      <head>
         <title>Hello {name}</title>
       </head>
       <body>
         <h1>Hello {name}!</h1>
       </body>
    </html>"""

    def hello_world(environ, start_response):
        start_response("200, OK", [("Content-type", "text/html")])
        params = environ["params"]
        resp = _hello_resp.format(name=params.get("name"))
        yield resp.encode("utf-8")

    _localtime_resp = """\
    <?xml version="1.0"?>
    <time>
      <year>{t.tm_year}</year>
      <month>{t.tm_mon}</month>
      <day>{t.tm_mday}</day>
      <hour>{t.tm_hour}</hour>
      <minute>{t.tm_min}</minute>
      <second>{t.tm_sec}</second>
    </time>"""

    def localtime(environ, start_response):
        start_response("200 OK", [("Content-type", "application/xml")])
        resp = _localtime_resp.format(t=time.localtime())
        yield resp.encode("utf-8")

    from wsgiref.simple_server import make_server

    # create the dispatcher and register functions
    dispatcher = PathDispatcher()
    dispatcher.register("GET", "/hello", hello_world)
    dispatcher.register("GET", "/localtime", localtime)

    # launch a basic server
    httpd = make_server("", 8080, dispatcher)
    print("Serving on port 8080...")
    httpd.serve_forever()
