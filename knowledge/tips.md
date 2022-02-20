#### 不清楚的地方
__new__
map()
lamda
list， dict的方法
python的GIL
fun(*args,**kwargs)
装饰器
with
random模块的方法
字符串r"/hi"
正则
assert
SQL distinct
Linux常用命令
python2与python3的区别
内置函数sorted()，filter()
collections的方法
删除文件操作
数据库基本方法及优化查询（外键，索引，联合查询，选择特定字段）
自定义异常
Django的orm
字符串join
try except else
try except finally
zip()
myaql和redis的区别
类的各种方法 魔法方法， 单例模式
round()的用法以及%0.03f
http状态码

cookie和session
多进程，多线程
any(), all()
python中什么元素为假
sort(), sorted()
lamda结合sorted等
递归
json和python字典转化
文件打开模式
python垃圾回收机制




1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；

2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。

3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。










48、提高python运行效率的方法

1、使用生成器，因为可以节约大量内存

2、循环代码优化，避免过多重复代码的执行

3、核心模块用Cython PyPy等，提高效率

4、多进程、多线程、协程

5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率


57、分别从前端、后端、数据库阐述web项目的性能优化

该题目网上有很多方法，我不想截图网上的长串文字，看的头疼，按我自己的理解说几点

前端优化：

1、减少http请求、例如制作精灵图

2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差



后端优化：

1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。

2、异步方式，如果有耗时操作，可以采用异步，比如celery

3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况



数据库优化：

1、如有条件，数据可以存放于redis，读取速度快

2、建立索引、外键等

65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常

IOError：输入输出异常

AttributeError：试图访问一个对象没有的属性

ImportError：无法引入模块或包，基本是路径问题

IndentationError：语法错误，代码没有正确的对齐

IndexError：下标索引超出序列边界

KeyError:试图访问你字典里不存在的键

SyntaxError:Python代码逻辑语法出错，不能执行

NameError:使用一个还未赋予对象的变量