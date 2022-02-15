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