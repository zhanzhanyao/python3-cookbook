#### Data  Structures and Algorithms
Separate the sequence(any iterable object) into individual variables  

    name, shares, price, date = data  
    _, shares, price, _ = date  
    *ign, tail = data

Reserve last several elements 

    from collections import deque  
    previous_lines = deque(maxlen=3) 
        
    q.extendleft([1, 2, 3, 4])  
    q.appendleft(0)  
    q.popleft()

Search the largest or smallest N elements  

    import heapq  
 
    largest_nums = heapq.nlargest(3, nums)  
    smallest_nums = heapq.nsmallest(3, nums)  

    expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])   

Queue sorted by priority, every pop operation will get the highest priority element  

    import heapq    

    heapq.heappush(self._queue, (-priority, self._index, item))
    heapq.heappop(self._queue)[-1]

Delete duplicate and keep original order in sequence

    def deldupe_1(items):
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)

Usage of yield

    def fab(max_n):
        n, a, b = 0, 0, 1
        while n < max_n:
            yield b
            # yield create a generator to avoid costs in memory, batter than store in list
            a, b = b, a + b
            n += 1

Usage of slice

    SHARES = slice(20, 23)
    PRICES = slice(31, 37)
    cost = float(record[SHARES]) * float(record[PRICES])
    
    # Avoiding IndexError
    a = slice(5, 50, 2)
    s = "GoodMorning"
    for i in range(a.indices(len(s))):
        print(s[i])

Usage of counter  

    from collections import Counter

    word_counts = Counter(words)
    top = word_counts.most_common(3)

Sort objects that can not be compared

    from operator import attrgetter

    sorted(users, key=attrgetter("user_id"))

Name the value of the tuple

    from collections import namedtuple

    Subscriber = namedtuple("Subscriber", ["addr", "joined"])
    sub = Subscriber("940105829@qq.com", "2021/12/12")
    sub.addr  # 940105829@qq.com
    sub.joined  # 2021/12/12

Generator

    s = sum(x * x for x in nums)

Combine more than one dict

    from collections import ChainMap

    c = ChainMap(a, b) 

Create multiply dict: one key corresponds to multiple values

    from collections import defaultdict  
    
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)

Create ordered dict

    from collections import OrderedDict

    dict = OrderedDict()

Operate dict

    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    price_sorted = sorted(zip(prices.values(), prices.keys()))

Set operations in dict

    a.keys() & b.keys()
    a.keys() - b.keys()
    a.items() & b.items()
    c = {key: a[key] for key in a.keys() - {"z", "w"}}


Group dict

    from itertools import groupby
    from operator import itemgetter

    # sort by desired field first because groupby optration work on continuous records
    rows.sort(key=itemgetter("date"))
    groupby(rows, key=itemgetter("date"))

Select desired values from a dict

    p1 = {key: value for key, value in prices.items() if value > 200}

Operations in multiple dict_list

    from operator import itemgetter

    sorted(rows, key=lambda a: a["uid"])
    sorted(rows, key=itemgetter("uid"))  # faster

    min(rows, key=itemgetter("uid"))
    max(rows, key=itemgetter("uid"))

Select desired values from a list

    newgenrt = (n for n in mylist if n > 0)  # small memory cost
    new_list = [n if n > 0 else 0 for n in mylist]

    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values))

    from itertools import compress
    mores = [n > 5 for n in counts]  # [False, False, True, False, False, True, True, False]
    list(compress(addresses, mores))  # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']