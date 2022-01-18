from collections import deque


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
    q=deque()
    q.extendleft([1,2,3,4])
    q.appendleft(0)
    q.popleft()
