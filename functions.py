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
