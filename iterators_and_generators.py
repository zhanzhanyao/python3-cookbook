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