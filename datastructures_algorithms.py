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

    """Search largest or smallest N elements for a composite data structure"""
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

    """
    Notice:
    1. heap is used in N is much less than than the length of input
    2. N is near the length of input, use sorted(items)[:N]
    3. Search one largest/smallest using max(),min()
    """


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
    s.setdefault("a",[])
    s.setdefault("b",[])

    pairs = ("a", 1)
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = value
        d[key].append(value)

    d=defaultdict(list)
    for key, value in pairs:
        d[key].append(value)


create_multdict()