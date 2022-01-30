import ntpath


def wr_csv():
    """Use Python to process data encoded in a variety of ways"""
    # read csv
    import csv

    with open("stocks.csv") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        # print(headers)
        for row in f_csv:
            pass

    # named tuple
    from collections import namedtuple

    with open("stocks.csv") as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple("Row", headings)
        for r in f_csv:
            row = Row(*r)
            # print(row.Price)

    # read csv to dict
    import csv

    with open("stocks.csv") as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row)

    # write to csv
    headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
    rows = [
        ("AA", 39.48, "6/11/2007", "9:36am", -0.18, 181800),
        ("AIG", 71.38, "6/11/2007", "9:36am", -0.15, 195500),
        ("AXP", 62.58, "6/11/2007", "9:36am", -0.46, 935000),
    ]

    with open("stock.csv", "w") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    # write dict to csv
    headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]
    rows = [
        {
            "Symbol": "AA",
            "Price": 39.48,
            "Date": "6/11/2007",
            "Time": "9:36am",
            "Change": -0.18,
            "Volume": 181800,
        },
        {
            "Symbol": "AIG",
            "Price": 71.38,
            "Date": "6/11/2007",
            "Time": "9:36am",
            "Change": -0.15,
            "Volume": 195500,
        },
        {
            "Symbol": "AXP",
            "Price": 62.58,
            "Date": "6/11/2007",
            "Time": "9:36am",
            "Change": -0.46,
            "Volume": 935000,
        },
    ]

    with open("stocks.csv", "w") as f:
        f_csv = csv.DictWriter(f)
        f_csv.writeheader()
        f_csv.writerows(rows)


def wr_json():
    import json

    # dict to json
    data = {"name": "ACME", "shares": 100, "price": 542.23}
    json_str = json.dumps(data)
    # json to dict
    data = json.loads(json_str)

    # writing JSON data
    with open("data.json", "w") as f:
        json.dump(data, f)

    # JSON file to data
    with open("data.json", "r") as f:
        data = json.load(f)


def parse_xml():
    """Extract data from XML"""
    from urllib.request import urlopen
    from xml.etree.ElementTree import parse

    # Download the RSS feed and parse it
    u = urlopen("http://planet.python.org/rss20.xml")
    doc = parse(u)

    # Extract and output tags of interest
    for item in doc.iterfind("channel/item"):
        title = item.findtext("title")
        date = item.findtext("date")
        link = item.findtext("link")

        print(title)
        print(date)
        print(link)


def parse_huge_xml():
    """Parse huge xml files incrementally"""
    from xml.etree.ElementTree import iterparse

    def parse_and_remove(filename, path):
        path_parts = path.split("/")
        doc = iterparse(filename, ("start", "end"))
        # Skip the root element
        next(doc)

        tag_stack = []
        elem_stack = []
        for event, elem in doc:
            if event == "start":
                tag_stack.append(elem.tag)
                elem_stack.append(elem)
            elif event == "end":
                if tag_stack == path_parts:
                    yield elem
                    elem_stack[-2].remove(elem)
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass

    from collections import Counter

    potholes_by_zips = Counter()
    data = parse_and_remove("potholes.xml", "row/row")
    for pothole in data:
        potholes_by_zips[pothole.findtext("zip")] += 1
    for zipcode, num in potholes_by_zips.most_common():
        print(zipcode, num)


def dict_to_xml():
    """Store the data in a Python dictionary and convert it to XML format"""

    from xml.etree.ElementTree import Element

    def to_xml(tag, d):
        """Turn a simple dict of key/value pairs into XML"""
        elem = Element(tag)
        for key, val in d.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
        return elem

    s = {"name": "GOOG", "shares": 100, "price": 490.1}
    e = to_xml("stock", s)
    from xml.etree.ElementTree import tostring

    print(tostring(e))
    e.set("id", "1234")
    print(tostring(e))
