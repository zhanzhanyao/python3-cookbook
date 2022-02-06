def instance_repr():
    """change string representation of instances"""

    class pair:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return "Pair({0.x!r}, {0.y!r})".format(self)

        def __str__(self):
            return "({0.x!s}, {0.y!s})".format(self)

    p = pair(3, 4)
    print(str(p))  # (3, 4)
    print(repr(p))  # Pair(3, 4)


def instance_format():
    """customizing string formatting"""
    _formats = {
        "ymd": "{d.year}-{d.month}-{d.day}",
        "mdy": "{d.month}/{d.day}/{d.year}",
        "dmy": "{d.day}/{d.month}/{d.year}",
    }

    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        def __format__(self, code):
            if code == "":
                code = "ymd"
            fmt = _formats[code]
            return fmt.format(d=self)

    d = Date(2021, 12, 20)
    print(format(d))
    print(format(d, "mdy"))
    print(format(d, "dmy"))
    print("This day is {:dmy}".format(d))


def learn_with():
    """make objects support context management protocol"""
    from socket import socket, AF_INET, SOCK_STREAM

    class LazyConnection:
        def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
            self.address = address
            self.family = family
            self.type = type
            self.sock = None

        def __enter__(self):
            if self.sock is not None:
                raise RuntimeError("Already connected")
            self.sock = socket(self.family, self.type)
            self.sock.connect(self.address)
            return self.sock

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.sock.close()
            self.sock = None

    from functools import partial

    conn = LazyConnection(("www.python.org", 80))

    with conn as s:
        s.send(b"GET /index.html HTTP/1.0\r\n")
        s.send(b"Host: www.python.org\r\n")
        s.send(b"\r\n")
        resp = b"".join(iter(partial(s.recv, 8192), b""))

    class LazyConnection1:
        def __init__(self, address, family=AF_INET, TYPE=SOCK_STREAM):
            self.address = address
            self.family = family
            self.type = type
            self.connections = []

        def __enter__(self):
            sock = socket(self.family, self.type)
            sock.connect(self.address)
            self.connections.append(sock)
            return sock

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.connections.pop().close()

    conn = LazyConnection1(("www.python.org", 80))
    with conn as s1:
        pass
        with conn as s2:
            pass
