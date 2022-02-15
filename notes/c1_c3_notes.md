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


## Chapter 3: number date and time
### 1. round() 
四舍五入

### 2. format()
    format(x, '0.1f')

### 3. complex() 复数

### 4. math模块

### 5. numpy模块
    # 用来计算、处理一维或多维数组
    b=numpy.array([[1,2,3],[4,5,6]])
    b.shape  # 形状 
    b.dmin  # 维度
    b=b.reshape(3,2) 

    # 将python序列转换为ndarray
    l=[1,2,3,4,5,6,7] 
    a = np.asarray(l)
    
    # 定义结构化数据
    teacher = np.dtype([('name','S20'), ('age', 'i1'), ('salary', 'f4')])
    b = np.array([('ycs', 32, 6357.50),('jxe', 28, 6856.80)], dtype = teacher) 
    
    # 创建数组 
    np.zero()
    np.ones()
    
    # 创建区间数组
    np.arange(start, stop, step, dtype)
    
    # 索引
    
    # Broadcast
    
    # 迭代器
    np.nditer() 
    
    # 增删改查

### 6. random模块

### 7. datetime模块
    a = datetime(2012, 9, 23)

    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')

    datetime.datetime
    datetime.date
    datetime.time
    datetime.timedelta






