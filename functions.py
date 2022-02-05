def learn_args():
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
