# python3-cookbook note   

## Generator and Iterator    

### 1. next() 

    def __iter__(self):
        return iter(self._children)

### 2. yield

### 3. yield from

### 3. reversed()
- 反向迭代： 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表  
- 通过在自定义类上实现 __reversed__() 方法来实现反向迭代

### 4. itertools模块

### 5. enumerate()
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

### 6. zip()
同时迭代多个集合

### 7. instance()

## File and IO

### 1. with open("somefile") as f:
    with open('somefile.txt', 'rt', encoding='latin-1') as f:
            pass

### 2. print("xxx", seq="", end="")

### 3. io.StringIO
将字符串创建为类文件对象

    s = io.StringIO()
    s.write('Hello World\n')
    s.getvalue()

## 4. qzip bz2模块
读写压缩文件  

    import gzip
    with gzip.open('somefile.gz', 'rt') as f:
        text = f.read()

## 5. functools.partial()
一次读取固定大小数据块

    from functools import partial
    RECORD_SIZE = 32
    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            ...

## 6. os模块
进程参数  
文件描述符操作  
查询终端尺寸
文件与目录
Linux 扩展属性


## 7. io模块
文本IO
二进制IO




## 8. sys模块

## 9. pickle模块