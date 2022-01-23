def separate():
    """Separate the sequence(any iterable object) into individual variables"""
    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    # only need shares and price
    _, shares, price, _ = date
    ign, shares, price, ign = date

    # Separate uncertain quantity sequence
    head, *ign = data
    *ign, tail = data

    line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
    uname, *fields, homedir, sh = line.split(":")


def learn_deque():
    """Reserve last several elements"""
    from collections import deque

    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    # Example use on a file
    with open(r"../../cookbook/somefile.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-" * 20)

    # Use of deque
    q = deque()
    q.extendleft([1, 2, 3, 4])
    q.appendleft(0)
    q.popleft()


def learn_heap():
    """Search the largest or smallest N elements"""
    import heapq

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    largest_nums = heapq.nlargest(3, nums)
    smallest_nums = heapq.nsmallest(3, nums)

    # Search largest or smallest N elements for a composite data structure
    portfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
        {"name": "HPQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35},
        {"name": "ACME", "shares": 75, "price": 115.65},
    ]
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])

    # Notice:
    # 1. heap is used in N is much less than than the length of input
    # 2. N is near the length of input, use sorted(items)[:N]
    # 3. Search one largest/smallest using max(),min()


def learn_heap_1():
    """Queue sorted by priority, every pop operation will get the highest priority element"""
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]

    class Item:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return "Item({})".format(self.name)

    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("spam"), 4)
    q.push(Item("grok"), 1)
    q.pop()


def create_multdict():
    """One key corresponds to multiple values"""
    from collections import defaultdict

    d = defaultdict(list)
    d["a"].append(1)
    d["b"].append(4)

    s = {}
    s.setdefault("a", [])
    s.setdefault("b", [])

    pairs = ("a", 1)
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = value
        d[key].append(value)

    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)


def create_ordereddict():
    from collections import OrderedDict

    d = OrderedDict()
    # memory costs is more than general dict
    d["foo"] = 1
    d["bar"] = 2
    d["spam"] = 3
    d["grok"] = 4
    for key in d:
        print(key, d[key])

    # Using OrderedDict() to control JSON sequence
    import json

    json.dump(d)


def operate_dict():
    prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    price_sorted = sorted(zip(prices.values(), prices.keys()))
    # notice: iterator created by zip only can be operated one time


def common_in_dict():
    a = {"x": 1, "y": 2, "z": 3}
    b = {"w": 10, "x": 11, "y": 2}

    # common keys
    a.keys() & b.keys()
    # keys in a not in b
    a.keys() - b.keys()
    # common (key, value)
    a.items() & b.items()
    # pairs' key are not {"z","w"}
    c = {key: a[key] for key in a.keys() - {"z", "w"}}


def deldupe():
    """Delete duplicate and keep original order in sequence"""

    def deldupe_1(items):
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    deldupe_1(a)  # [1, 5, 2, 9, 10]

    def deldupe_2(items, key=None):
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

    a = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]
    deldupe_2(
        a, key=lambda b: (b["x"], b["y"])
    )  # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
    deldupe_2(a, key=lambda b: b["x"])  # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


def fab(max_n):
    n, a, b = 0, 0, 1
    while n < max_n:
        yield b
        # yield create a generator to avoid costs in memory, batter than store in list
        a, b = b, a + b
        n += 1


def learn_slice():
    record = "....................100.......513.25.........."
    SHARES = slice(20, 23)
    PRICES = slice(31, 37)
    cost = float(record[SHARES]) * float(record[PRICES])

    a = slice(5, 50, 2)
    s = "GoodMorning"
    # Avoiding IndexError
    for i in range(a.indices(len(s))):
        print(s[i])


def learn_counter():
    words = [
        "look",
        "into",
        "my",
        "eyes",
        "look",
    ]
    from collections import Counter

    word_counts = Counter(words)
    top = word_counts.most_common(3)


def operate_listdict():
    rows = [
        {"fname": "Brian", "lname": "Jones", "uid": 1003},
        {"fname": "David", "lname": "Beazley", "uid": 1002},
        {"fname": "John", "lname": "Cleese", "uid": 1001},
        {"fname": "Big", "lname": "Jones", "uid": 1004},
    ]
    from operator import itemgetter

    sorted(rows, key=lambda a: a["uid"])
    sorted(rows, key=itemgetter("uid"))  # faster

    min(rows, key=itemgetter("uid"))
    max(rows, key=itemgetter("uid"))


def sort_notcompare():
    """Sort object that doesn't support comparison"""

    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return "User({})".format(self.user_id)

    def sort_nocompare():
        users = [User(23), User(10), User(2)]
        print(sorted(users, key=lambda a: a.user_id))

    def sort_nocompare_1():
        users = [User(23), User(10), User(2)]
        from operator import attrgetter

        sorted(users, key=attrgetter("user_id"))


def group_dict():
    rows = [
        {"address": "5412 N CLARK", "date": "07/01/2012"},
        {"address": "5148 N CLARK", "date": "07/04/2012"},
        {"address": "5800 E 58TH", "date": "07/02/2012"},
        {"address": "2122 N CLARK", "date": "07/03/2012"},
        {"address": "5645 N RAVENSWOOD", "date": "07/02/2012"},
        {"address": "1060 W ADDISON", "date": "07/02/2012"},
        {"address": "4801 N BROADWAY", "date": "07/01/2012"},
        {"address": "1039 W GRANVILLE", "date": "07/04/2012"},
    ]
    # Group and access the sequence
    from itertools import groupby
    from operator import itemgetter

    # sort by desired field first because groupby optration work on continuous records
    # rows = sorted(rows,key=itemgetter("date"))
    rows.sort(key=itemgetter("date"))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter("date")):
        print(date)
        for i in items:
            print(i)

    from collections import defaultdict

    rows_by_date = defaultdict()
    for row in rows:
        rows_by_date[row["date"]].append(row)

    for i in rows_by_date["07/01/2012"]:
        print(i)


def learn_listfilter():
    """Select desired values from a list"""
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    newlist = [n for n in mylist if n > 0]  # large memory cost
    newgenrt = (n for n in mylist if n > 0)  # small memory cost
    for i in newgenrt:
        print(i)

    # complex filter
    values = ["1", "2", "-3", "-", "4", "N/A", "5"]

    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False

    ivals = list(filter(is_int, values))
    print(ivals)

    # Filter and replace by desired value
    new_list = [n if n > 0 else 0 for n in mylist]

    addresses = [
        "5412 N CLARK",
        "5148 N CLARK",
        "5800 E 58TH",
        "2122 N CLARK",
        "5645 N RAVENSWOOD",
        "1060 W ADDISON",
        "4801 N BROADWAY",
        "1039 W GRANVILLE",
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    from itertools import compress

    mores = [
        n > 5 for n in counts
    ]  # [False, False, True, False, False, True, True, False]
    list(
        compress(addresses, mores)
    )  # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']


def learn_dicefilter():
    """Select desired values from a dict"""
    prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}
    p1 = {key: value for key, value in prices.items() if value > 200}
    p2 = {key: value for key, value in prices.items() if key == "AAPL"}


def learn_namedtup():
    from collections import namedtuple

    Subscriber = namedtuple("Subscriber", ["addr", "joined"])
    sub = Subscriber("940105829@qq.com", "2021/12/12")
    sub.addr  # 940105829@qq.com
    sub.joined  # 2021/12/12

    Stock = namedtuple("Stock", ["name", "shares", "price"])
    # Avoid operate elements by subscript
    def compute_cost(records):
        total = 0.0
        for rec in records:
            s = Stock(*rec)
            total += s.shares * s.price
            return total

    # Replace Dict to reduce memory costs
    Stock = namedtuple("Stock", ["name", "shares", "price", "date", "time"])
    # Create a prototype instance
    stock_prototype = Stock("", 0, 0.0, None, None)
    a = {"name": "ACME", "shares": 100, "price": 123.45}
    s = stock_prototype._replace(**a)
    print(s)


def learn_generator():
    """Transform and calculate a sequence simultaneously"""
    nums = [1, 2, 3, 4, 5]
    s = sum(n for n in nums)

    # Determine if any .py files exist in a directory
    import os

    files = os.listdir("dirname")
    if any(name.endswith(".py") for name in files):
        print("Python file exists")
    else:
        print("No python file")

    # Output a tuple as csv
    s = ("ACME", 50, 123.45)
    print(",".join(str(x) for x in s))

    # Data reduction across fields of a data structure
    portfolio = [
        {"name": "GOOG", "shares": 50},
        {"name": "YHOO", "shares": 75},
        {"name": "AOL", "shares": 20},
        {"name": "SCOX", "shares": 65},
    ]
    min_shares = min(s["shares"] for s in portfolio)
    min_shares = min(portfolio, key=lambda n: n["shares"])

    s = sum((x * x for x in nums))
    s = sum(x * x for x in nums)  # more elegant
    s = sum(
        [x * x for x in nums]
    )  # need to create a extra list, if list is very large, will cost many memories

def learn_chainmap():
    """Combine more than one dict"""
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    from collections import ChainMap
    c = ChainMap(a, b)  # if add value in a or b, value also be added into c

    merge = dict(a)
    merge.update(b)  # need to create a extra dict merge, and if add a new value in a,b, it will not be added into merge
