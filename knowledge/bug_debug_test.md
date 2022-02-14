# Bug Debug and Test
Bug: 程序编写问题
Exception：无法预测（磁盘，网络...）--> 异常处理机制
Debug 调试：跟踪程序执行，查看变量的值是否正确
Test：程序编写完成后运行测试，确保程序输出符合预期

## 1. 错误处理
### try...except...finally...
某些代码可能会出错时，就可以用try来运行这段代码；  
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块；  
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。  

        try:
            print('try...')
            r = 10 / 0
            print('result:', r)
        except ZeroDivisionError as e:
            print('except:', e)
        finally:
            print('finally...')
        print('END')
### 跨越多层调用
try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，  
比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，  
这时，只要main()捕获到了，就可以处理：

        def foo(s):
            return 10 / int(s)
        
        def bar(s):
            return foo(s) * 2
        
        def main():
            try:
                bar('0')
            except Exception as e:
                print('Error:', e)
            finally:
                print('finally...')

### 调用栈 callstack
不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了  

        Traceback (most recent call last):
          File "err.py", line 11, in <module>
            main()
          File "err.py", line 9, in main
            bar('0')
          File "err.py", line 6, in bar
            return foo(s) * 2
          File "err.py", line 3, in foo
            return 10 / int(s)
        ZeroDivisionError: division by zero

### 记录错误
Python内置的logging模块可以非常容易地记录错误信息：  
        
        import logging
        
        def foo(s):
            return 10 / int(s)
        def bar(s):
            return foo(s) * 2
        def main():
            try:
                bar('0')
            except Exception as e:
                logging.exception(e)
        
        main()
        # 程序打印完错误信息后会继续执行
        print('END')

### 抛出错误
定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例

        class FooError(ValueError):
            pass
        
        def foo(s):
            n = int(s)
            if n==0:
                raise FooError('invalid value: %s' % s)
            return 10 / n
        
        foo('0')

捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。  


        def foo(s):
            n = int(s)
            if n==0:
                raise ValueError('invalid value: %s' % s)
            return 10 / n
        
        def bar():
            try:
                foo('0')
            except ValueError as e:
                print('ValueError!')
                raise
        
        bar()

## 2. 调试
- print()
- assert
- logging
- pdb
- IDE

## 3. 单元测试
- 单元测试：对一个模块、一个函数或者一个类来进行正确性检验的测试工作  
- unittest模块  
- setUp与tearDown：分别在每调用一个测试方法的前后分别被执行

## 4. 文档测试

        class Dict(dict):
            '''
            Simple dict but also support access as x.y style.
        
            >>> d1 = Dict()
            >>> d1['x'] = 100
            >>> d1.x
            100
            >>> d1.y = 200
            >>> d1['y']
            200
            >>> d2 = Dict(a=1, b=2, c='3')
            >>> d2.c
            '3'
            >>> d2['empty']
            Traceback (most recent call last):
                ...
            KeyError: 'empty'
            >>> d2.empty
            Traceback (most recent call last):
                ...
            AttributeError: 'Dict' object has no attribute 'empty'
            '''
            def __init__(self, **kw):
                super(Dict, self).__init__(**kw)
        
            def __getattr__(self, key):
                try:
                    return self[key]
                except KeyError:
                    raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
        
            def __setattr__(self, key, value):
                self[key] = value
        
        if __name__=='__main__':
            import doctest
            doctest.testmod()
