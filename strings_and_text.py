import re


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


def match_string():
    """Match start and end of text"""
    filename = f"p02_match_text_at_start_end.txt"
    filename.endswith(".txt")  # True
    filename.startswith(".txt")  # False

    import os

    filenames = os.listdir(".")  # [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
    targetfile = [
        name for name in filenames if name.endswith((".c", ".h"))
    ]  # ['foo.c', 'spam.c', 'spam.h'
    if any(name.endswith(".py") for name in filenames):
        pass


def match_string_1():
    """match strings with shell wildcard"""
    from fnmatch import fnmatch, fnmatchcase

    fnmatch("foo.txt", "*.txt")  # True
    fnmatch("foo.txt", "?oo.txt")  # True
    fnmatch("Data45.txt", "Data[0-9]*.txt")  # True
    names = ["Dat1.csv", "Dat2.csv", "config.ini", "foo.py"]
    target = [
        name for name in names if fnmatch(name, "*.csv")
    ]  # ['Dat1.csv', 'Dat2.csv']

    fnmatch("foo.txt", "*.TXT")  # on mac-->False, on windows-->True
    fnmatchcase("foo.txt", "*.TXT")  # False


def match_string_2():
    """Summary of string searching and matching"""
    # simple matching
    text = "yeah, but no, but yeah, but no, but yeah"
    text == "yeah, but no, but yeah"  # false
    text.endswith("yeah")  # true
    text.startswith("yeah")  # true
    text.find("no")  # 10

    # complex matching
    text1 = "11/27/2012"
    import re

    if re.Match(r"\d+/\d+/\d+", text1):
        pass

    # pattern
    datepat = re.compile(r"\d+/\d+/\d+")
    if datepat.match(text1):
        pass

    # find first one/find all
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    datepat.findall(text)  # ['11/27/2012', '3/13/2013']

    # group the result
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    m = datepat.match(text1)
    m.groups()  # ('11', '27', '2012')

    # return a iterator
    datepat.finditer(text1)


def replace_text():
    """Text searching and replacing"""
    # simple seaching
    text = "yeah, but no, but yeah, but no, but yeah"
    print(text.replace("yeah", "yep"))

    # regex searching
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    import re

    re.sub(
        r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text
    )  # 'Today is 2012-11-27. PyCon starts 2013-3-13.'

    # pattern
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    datepat.sub(r"\3-\1-\2", text)  # 'Today is 2012-11-27. PyCon starts 2013-3-13.'

    # named regex
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)/",
        r"\g<year>-\g<month>-\g<day>-",
        text,
    )

    #
    from calendar import month_abbr
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return "{}{}{}".format(m.group(2, mon_name, m.group(3)))

    datepat.sub(change_date, text)

def search_insensitive():
    """Text searching and replacing insensitive"""
    text = 'UPPER PYTHON, lower python, Mixed Python'
    re.findall(r"python", text, flags=re.IGNORECASE)  # ['PYTHON', 'python', 'Python']
    re.sub("python","snake",tags=re.IGNORECASE)

    # replace and initial case keep consistent
    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word
        return replace

    re.sub("python", matchcase("snake"), text, tags=re.IGNORECASE)
