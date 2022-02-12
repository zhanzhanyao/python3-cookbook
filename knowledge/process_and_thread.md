# 进程和线程
- 对于操作系统来说，一个任务就是一个进程（Process）   
- 在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）  
- 多任务  
    - 多进程模式
    - 多线程模式
    - 多进程+多线程模式
## 1. 多进程（multiprocessing）
### on Unix/Linux/MAC
Python的os模块封装了常见的系统调用。    

        # 在python程序创建子进程
        import os
        print("process {} start". format(os.getpid()))
        # on Unix/Linux/MAC
        pid = os.fork()
        if pid == 0:
            print("child process {}, parent process is {}".format(os.getpid(), os.getppid()))
        else:
            print("parent process{}, child process is {}".format(pid, os.getpid()))

有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务。  

### multiprocessing 模块
要实现跨平台的多进程， multiprocessing模块提供了一个Process类来代表一个进程对象  

        # 创建一个子进程并等待其结束
        from multiprocessing import Process
        import os
        
        # 子进程要执行的代码
        def run_proc(name):
            print("Run child process {}({})".format(name, os.getpid()))
        
        print("parent process {}".format(os.getpid()))
        p = Process(target=run_proc, args=("test",))
        print("Child process will start")
        p.start()
        p.join()
        print("child process end")

### Pool
启动大量的子进程，可以用进程池的方式批量创建子进程。  

    from multiprocessing import Pool
    
    def long_time_task(name):
        print("run task {}({})".format(name, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print("task {} run {} seconds".format(name, (end - start)))
    
    
    print("parent process {} start".format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("waiting for all subprocesses done...")
    p.close()
    p.join()
    print("all subprocesses done")

### 子进程
子进程并不是自身，而是一个外部进程时，创建了子进程后，还需要控制子进程的输入和输出。  
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。  

    import subprocess
    
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

### 进程间通信
进程间通信是通过Queue、Pipes等实现的  

    from multiprocessing import Process, Queue
    import os, time, random
    
    # 写数据进程执行的代码:
    def write(q):
        print('Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(random.random())
    
    # 读数据进程执行的代码:
    def read(q):
        print('Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)
            print('Get %s from queue.' % value)
    
    if __name__=='__main__':
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()
        pw = Process(target=write, args=(q,))
        pr = Process(target=read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()


## 2. 多线程
- 进程是由若干线程组成，多任务可以由多进程完成，也可以由一个进程内的多线程完成。  
- Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。    


        import time, threading
        
        # 新线程执行的代码:
        def loop():
            print('thread %s is running...' % threading.current_thread().name)
            n = 0
            while n < 5:
                n = n + 1
                print('thread %s >>> %s' % (threading.current_thread().name, n))
                time.sleep(1)
            print('thread %s ended.' % threading.current_thread().name)
        
        print('thread %s is running...' % threading.current_thread().name)
        t = threading.Thread(target=loop, name='LoopThread')
        t.start()
        t.join()
        print('thread %s ended.' % threading.current_thread().name)

### Lock
多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改.  

    balance = 0
    lock = threading.Lock()
    
    def run_thread(n):
        for i in range(100000):
            # 先要获取锁:
            lock.acquire()
            try:
                # 放心地改吧:
                change_it(n)
            finally:
                # 改完了一定要释放锁:
                lock.release()

- 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。  
- Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。  

## 3. ThreadLocal
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。  


    import threading
        
    # 创建全局ThreadLocal对象:
    local_school = threading.local()
    
    def process_student():
        # 获取当前线程关联的student:
        std = local_school.student
        print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
    def process_thread(name):
        # 绑定ThreadLocal的student:
        local_school.student = name
        process_student()
    
    t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

## 4. 进程 vs. 线程
多任务：Master+Worker模式
- Master：分配任务
- Worker：执行任务  
##### 多进程  
- 稳定性高，一个子进程崩溃，不会影响主进程与其他子进程
- 创建进程代价大；操作系统同时进行的进程数有限（CPU，内存限制）   
##### 多线程  
- 比多进程略快
- 一个线程挂掉导致整个进程崩溃（所有线程共享进程的内存）

### 线程切换
操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。  

### 任务类型
是否采用多任务的第二个考虑是任务的类型。
- 计算密集型：主要消耗CPU资源
- IO密集型： 涉及到网络，磁盘IO的任务。Web应用

### 异步IO
- 事件驱动模型： 充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务  
- 对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。

## 5. 分布式进程
- Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
- 把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。  


    # refer to: distributed_process.py
