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
