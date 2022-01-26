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

def learn_enumerate():
    """iterate over index value pairs of sequence"""
    my_list = ["a","b","c"]
    for idx,value in enumerate(my_list, 1):
        print(idx,value,sep=":")

    def parse_data(filename):
        with open(filename, "rt") as f:
            for lineno, line in enumerate(f,1):
                field = line.split()
                try:
                    count = field[1]
                except ValueError as e:
                    print("Line {}: parse error:{}".format(lineno, e))

    from collections import defaultdict
    word_summary = defaultdict(list)
    with open("file.txt", "r") as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)

def learn_zip():
    """iterate over multiple sequences simultaneously"""
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts,ypts):
        print(x,y)
    from itertools import chain
    """iterate on items in separate containers"""
    for x in chain(xpts,ypts):
        print(x)

def iter_pipeline():
    """Create data processing pipelines"""
    import os
    import fnmatch
    import gzip
    import bz2
    import re


    def gen_find(filepat, top):
        """Find all filenames in a directory tree that match a shell wildcard pattern"""
        for path, dirlist, filelist in os.walk():
            for name in fnmatch.filter(filelist,filepat):
                yield os.path.join(path, name)


    def gen_opener(filenames):
        """
        Open a sequence of filenames one at a time producing a file object.
        The file is closed immediately when proceeding to the next iteration.
        """
        for filename in filenames:
            if filename.endwith(".gz"):
                f = gzip.open(filename,"rt")
            elif filename.endwith(".bz2"):
                f =bz2.open(filename,"rt")
            else:
                f = open(filename,"rt")
            yield f
            f.close()


    def gen_concatenate(iterator):
        """
        Chain a sequence of iterators together into a single sequence
        """
        for it in iterator:
            yield  from it


    def gen_grep(pattern, lines):
        """
        Look for a regex pattern in q sequence of lines
        """
        pat = re.compile(pattern)
        for line in lines:
            if pat.search(line):
                yield line

    logname = gen_find("access-log", "www")
    files = gen_opener(logname)
    lines = gen_concatenate(files)
    py_lines = gen_grep("(?i)python", lines)
    bytecolumn = (line.rsplit(None, 1)[1]for line in py_lines)
    bytes = (int(x) for x in bytecolumn if x != "-")
    print("Total", sum(bytes))
