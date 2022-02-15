# python3-cookbook note   

## Chapter 1 Data Structure and Algorithm    

### 1. collections 容器数据类型  
collections.deque 队列  
collections.multidict 多值字典   
collections.OrderedDict 排序字典  
collections.namedtuple 命名元组
collections.ChainMap 合并字典
collections.Counter  


### 2. heapq 堆
    heapq.nlargest()
    heapq.nsmallest()
    heapq.heappop()
    heapq.heappush()

### 3. operator模块
对象的比较运算  
逻辑运算  
数字运算  
序列运算  
operator.attrgetter 

    sorted(users, key=attrgetter('user_id'))

operator.itemgetter  

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
### 4.itertools


### 5. zip()
    prices_sorted = sorted(zip(prices.values(), prices.keys()))

### 6. lambda
    min_value = prices[min(prices, key=lambda k: prices[k])]
### 7. slice() 切片
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    items[a]

### 8. 列表推导式 生成器表达式


## Chapter 2 String and Text

### 1. re
    re.split(r'[;,\s]\s*', line)  
    re.compile(r'\d+/\d+/\d+') #模式对象  
    re.match()  
    re.sub() #替换
    re.findall()


### 2. string
    str.split()   
    str.endswith()  
    str.startswith()  
    str.find()
    str.finditer()
    
    str.replace()
    str.strip()
    
    str.join()
    str.format()

### 3. fnmatch 
shell风格的文件匹配  

    fnmatch.fnmatch()
    fnmatch.fnmatchcase()

