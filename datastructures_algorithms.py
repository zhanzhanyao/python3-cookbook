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
