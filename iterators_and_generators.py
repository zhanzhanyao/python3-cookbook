def consume_iterator():
    """manually consuming iterator"""

    def manual_iter():
        with open("/etc/passwd") as f:
            try:
                while True:
                    line = next(f)
                    print(line, end="")
            except StopIteration:
                pass


def delegate_iter():
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return "Node({!r})".format(self._value)

        def add_children(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for ch in root:
        print(ch)


def create_iter():
    """create new iteration with generators"""

    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    for n in frange(1, 10, 2):
        print(n)


def implement_iter():
    """implement iterator protocol"""

    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return "Node({！r})".format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):
            return iter(self._children)

        def depth_first(self):
            yield self
            for c in self:
                yield from c.depth_first()

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)


def iter_reserve():
    """iterating in reverse"""

    class Countdown:
        def __init__(self, start):
            self.start = start

        # forward iterator
        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        # reserved iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1

    for rr in Countdown(30):
        print(rr)

    for rr in reversed(Countdown(30)):
        print(rr)


def learn_generator():
    """define generator func with extra state"""
    from collections import deque

    class linehistory:
        def __init__(self, lines, histlen=3):
            self.lines = lines
            self.history = deque(maxlen=histlen)

        def __iter__(self):
            for lineno, line in enumerate(self.lines, 1):
                self.history.append((lineno, line))
                yield line

        def clear(self):
            self.history.clear()

    with open("somefile.txt") as f:
        lines = linehistory(f)
        for line in lines:
            if "python" in line:
                for lineno, hline in lines.history:
                    print("{}:{}".format(lineno, hline), end="")

    f = open("somefile.txt")
    lines = linehistory(f)
    it = iter(lines)  # If do not use for-loop, call iter() first
    next(it)

def iter_tip():
    """Taking slice of iterator"""
    def count(n):
        while True:
            yield n
            n += 1


    import itertools

    c = count(0)  # c in a generator, can't be sliced
    for i in itertools.islice(c, 10, 20):
        print(i)

    """Skip first part of iterable"""
    from itertools import dropwhile

    with open("/etc/passwd") as f:
        for line in dropwhile(lambda line: not line.startwith("#"), f):
            print(line, end="")


    """Skip elements with certain location"""
    from itertools import islice

    items = ["a", "b", "c", "d", 1, 2, 3]
    for x in islice(items,4,None):
        print(x)