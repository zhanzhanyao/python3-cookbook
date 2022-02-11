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
