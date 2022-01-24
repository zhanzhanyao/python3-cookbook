def split_string():
    """Split a string by multiple delimiters"""
    line = "asdf fjdk; afed, fjek,asdf, foo"
    import re

    # Split this string
    re.split(r"[;,\s]\s*", line)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    re.split(
        r"(;|,|\s)\s*", line
    )  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    # Reform this string
    field = re.split(
        r"(;|,|\s)\s*", line
    )  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    values = field[::2]
    delimiters = field[1::2]
    line = "".join(v + d for v, d in zip(values, delimiters))
