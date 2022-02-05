def learn_params():
    """functions that accept any number arguments"""

    def avg(first, *rest):
        return (first + sum(rest)) / (1 + len(rest))

    print(avg(1, 2))
    print(avg(1, 2, 3, 4))

    import html

    def make_element(name, value, **attrs):
        keyvals = ["%s='%s'" % item for item in attrs.items()]
        attr_str = "".join(keyvals)
        element = "<{name}{attrs}>{value}</{name}>".format(
            name=name,
            attrs=attr_str,
            value=html.escape(value),
        )
        return element

    make_element("item", "Albatross", size="large", qualitity=6)

    def anyargs(*args, **kwargs):
        print(args)  # ()
        print(kwargs)  # {}


def learn_params_1():
    """functions that only accept keyword arguments"""

    def recv(maxsize, *, block):
        pass

    recv(1021, block=True)

    def minmum(*value, clip=None):
        m = min(value)
        if clip is not None:
            m = clip if clip > m else m
            return m


def func_matadata():
    """attach informatinal matadata to function parameters"""

    def add(x: int, y: int) -> int:
        return x + y

    help(add)


def default_params():
    """
    define functions with default arguments
    default parameters must be immutable types.
    """

    def spam(a, b=42):
        # param is a value
        print(a, b)

    def spam1(a, b=None):
        # param is a list
        if b is None:
            b = []

    # check if a desired default parameter is inputted
    _no_value = object()

    def spam2(a, b=_no_value):
        if b is _no_value:
            print("No b value supplied")


def learn_closure():
    from urllib.request import urlopen

    class UrlTemplate:
        def __init__(self, template):
            self.template = template

        def open(self, **kwargs):
            return urlopen(self.template.format_map(kwargs))

    yahoo = UrlTemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
    for line in yahoo.open(names="IBM,AAPL,FB", fields="sl1clv"):
        print(line.decode("utf-8"))

    def urltemplate(template):
        def opener(**kwargs):
            return urlopen(template.format_map(kwargs))

        return opener

    yahoo = urltemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
    for line in yahoo(names="IBM,AAPL,FB", fields="sl1clv"):
        print(line.decode("utf-8"))
