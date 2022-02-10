import bisect


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


# def learn_slots:
# save memory when create large number instances


def learn_property():
    """create managed attributes"""

    class Person:
        def __init__(self, first_name):
            self._first_name = first_name

        @property
        def first_name(self):
            return self._first_name

        @first_name.setter
        def first_name(self, value):
            if not isinstance(value, str):
                raise TypeError("Expected a string")
            self._first_name = value

        @first_name.deleter
        def first_name(self):
            raise AttributeError("Can't delete attribute")

    a = Person("Yao")
    print(a.first_name)

    a.first_name = 12  # TypeError: Expected a string
    del a.first_name  # AttributeError: Can't delete attribute


def learn_descripter():
    """create new kind of class or instance attribute"""

    class Integer:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError("Expected an int")
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            del instance.__dict[self.name]

    class Point:
        x = Integer("x")
        y = Integer("y")

        def __init__(self, x, y):
            self.x = x
            self.y = y

    p = Point(2, 3)
    p.x = 2.5
    print(p.x)


def learn_descripter():
    """using lazily computed properties"""

    class lazyproperty:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                value = self.func(instance)
                setattr(instance, self.func.__name__, value)
                return value

    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @lazyproperty
        def area(self):
            print("Computing area")
            return math.pi * self.radius ** 2

        @lazyproperty
        def perimeter(self):
            print("Computing perimeter")
            return 2 * math.pi * self.radius

    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.area)


def simp_init():
    """simplify initialization of data structure"""
    import math

    class Structure1:
        # class variable that specifies expected fields
        _fields = []

        def __init__(self, *args):
            if len(args) != len(self._fields):
                raise TypeError("Expected {} arguments".format(len(self._fields)))
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

    class Stock(Structure1):
        _fields = ["name", "shares", "price"]

    class Point(Structure1):
        _fields = ["x", "y"]

    class Circle(Structure1):
        _fields = ["radius"]

        def area(self):
            return math.pi * self.radius ** 2

    s = Stock("ACME", 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)
    S2 = Stock("ACME", 50)  # TypeError: Expected 3 arguments

    class Structures2:
        _fields = []

        def __init__(self, *args, **kwargs):
            if len(args) > len(self._fields):
                raise TypeError("Expected {} arguments".format(len(self._fields)))

            # set all of the positional arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

            # set the remaining keyword arguments
            for name in self._fields[len(args)]:
                setattr(self, name, kwargs.pop(name))

            # check for any remaining unknown arguments
            if kwargs:
                raise TypeError("Invalid argument(s): {}".format(",".join(kwargs)))

    s1 = Stock("ACME", 50, 91.1)
    s2 = Stock("ACME", 50, price=91.1)
    s3 = Stock("ACME", shares=50, price=91.1)


def learn_abstract_class():
    """define interface or abstract base class"""
    from abc import ABCMeta, abstractmethod

    class Istream(metaclass=ABCMeta):
        @abstractmethod
        def read(self, maxbytes=-1):
            pass

        @abstractmethod
        def write(self, data):
            pass

    class SocketStream(Istream):
        def read(self, maxbytes=-1):
            pass

        def write(self, data):
            pass


def imple_datamodel():
    """implementing data model or type system"""

    class Descriptor:
        # Base class. uses a descriptor to set a value
        def __init__(self, name=None, **opts):
            self.name = name
            for key, value in opts.items():
                setattr(self, key, value)

        def __set__(self, instance, value):
            instance.__dict_[self.name] = value

    # Descriptor for enforcing types
    class Typed(Descriptor):
        expected_type = type(None)

        def __set__(self, instance, value):
            if not isinstance(value, self.expected_type):
                raise TypeError("expected" + str(self.expected_type))
            super().__set__(instance, value)

    # Descriptor for enforcing values
    class Unsigned(Descriptor):
        def __set__(self, instance, value):
            if value < 0:
                raise ValueError("Expected < 0")
            super().__set__(instance, value)

    class MaxSize(Descriptor):
        def __init__(self, name=None, **opts):
            if "size" not in opts:
                raise TypeError("missing size option")
            super().__init__(name, **opts)

        def __set__(self, instance, value):
            if len(value) >= self.size:
                raise ValueError("size must be <" + str(self.size))
            super.__set__(instance, value)

    class Integer(Typed):
        expected_type = int

    class UnsignedInteger(Integer, Unsigned):
        pass

    class Float(Typed):
        expected_type = float

    class UnsignedFloat(Float, Unsigned):
        pass

    class String(Typed):
        expected_type = str

    class SizedString(String, MaxSize):
        pass

    class Stock:
        # specify constraints
        name = SizedString("name", size=8)
        shares = UnsignedInteger("shares")
        price = UnsignedFloat("price")

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price


def learn_abstract_cls():
    """implemente custom containers"""
    import collections

    class SortedItems(collections.Sequence):
        def __init__(self, initial=None):
            self._items = sorted(initial) if initial is not None else []

        def __getitem__(self, index):
            return self._items[index]

        def __len__(self):
            return len(self._items)

        def add(self, item):
            bisect.insort(self._items, item)

    items = SortedItems([5, 1, 3])
    print(list(items))
    print(items[2])
    items.add(2)
    print(list(items))


def learn_state_object():
    """implements stateful objects or state machines"""

    class Connection:
        """Bad implementation that has complex code with too much if loops.Low efficiency"""

        def __init__(self):
            self.state = "CLOSED"

        def read(self):
            if self.state != "OPEN":
                raise RuntimeError("Not open")
            print("reading")

        def write(self, data):
            if self.state != "OPEN":
                raise RuntimeError("Not Open")
            print("writing")

        def open(self):
            if self.state == "OPEN":
                raise RuntimeError("Already open")
            self.state = "OPEN"

        def close(self):
            if self.state == "CLOSED":
                raise RuntimeError("Already closed")
            self.state = "CLOSED"

    class Connection1:
        def __init__(self):
            self.new_state(ClosedConnectionState)

        def new_state(self, newstate):
            self._state = newstate

        def read(self):
            return self._state.read(self)

        def write(self, data):
            return self._state.write(self, data)

        def open(self):
            return self._state.open(self)

        def close(self):
            return self._state.close(self)

    class ConnectionState:
        """connection state base class"""

        @staticmethod
        def read(cnn):
            raise NotImplementedError()

        @staticmethod
        def write(cnn, data):
            raise NotImplementedError()

        @staticmethod
        def open(cnn):
            raise NotImplementedError()

        @staticmethod
        def close(cnn):
            raise NotImplementedError()

    class ClosedConnectionState(ConnectionState):
        @staticmethod
        def read(cnn):
            raise RuntimeError("Not open")

        @staticmethod
        def write(cnn, data):
            raise RuntimeError("Not open")

        @staticmethod
        def open(cnn):
            cnn.new_state(OpenConnectionState)

        @staticmethod
        def close(cnn):
            raise RuntimeError("Already closed")

    class OpenConnectionState(ConnectionState):
        @staticmethod
        def read(cnn):
            print("reading")

        @staticmethod
        def write(cnn, data):
            print("writing")

        @staticmethod
        def open(cnn):
            raise RuntimeError("Already open")

        @staticmethod
        def close(cnn):
            cnn.new_state(ClosedConnectionState)

    c = Connection1()
    print(c._state)
    c.read()
    c.open()
    print(c._state)
    c.open()


def learn_visit_pattern():
    """implementing visitor pattern"""

    class Node:
        pass

    class UnaryOperator(Node):
        def __init__(self, operand):
            self.operand = operand

    class BinaryOperator(Node):
        def __init__(self, left, right):
            self.left = left
            self.right = right

    class Add(BinaryOperator):
        pass

    class Sub(BinaryOperator):
        pass

    class Mul(BinaryOperator):
        pass

    class Div(BinaryOperator):
        pass

    class Negate(UnaryOperator):
        pass

    class Number(Node):
        def __init__(self, value):
            self.value = value

    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    class NodeVisitor:
        def visit(self, node):
            methname = "visit_" + type(node).__name__
            meth = getattr(self, methname, None)
            if meth is None:
                meth = self.generic_visit
            return meth(node)

        def generic_visit(self, node):
            raise RuntimeError("No {} method".format("visit_" + type(node).__name__))

    class Evaluator(NodeVisitor):
        def visit_Number(self, node):
            return node.value

        def visit_Add(self, node):
            return self.visit(node.left) + self.visit(node.right)

        def visit_Sub(self, node):
            return self.visit(node.left) - self.visit(node.right)

        def visit_Mul(self, node):
            return self.visit(node.left) * self.visit(node.right)

        def visit_Div(self, node):
            return self.visit(node.left) / self.visit(node.right)

        def visit_Negate(self, node):
            return -node.operand

    e = Evaluator()
    print(e.visit(t4))

# skip the rest sections because it's difficult
