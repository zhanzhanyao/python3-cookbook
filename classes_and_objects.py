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
