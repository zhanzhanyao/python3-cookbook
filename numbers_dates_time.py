def round_number():
    round(1.23, 1)  # 1.2
    round(1.5, 0)  # 2
    round(101.5, -1)  # 100.0
    # format
    format(1.236, "0.2f")  # 1.24
    "value is {:0.2f}".format(1.236)  # value is 1.24
    # decimal module can make result precise


def learn_random():
    import random
    values = [1, 2, 3, 4, 5, 6]
    random.choice(values)
    random.sample(values, 3)
    random.shuffle(values)
    random.randint(0,9)
    random.random()