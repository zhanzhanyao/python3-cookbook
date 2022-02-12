# Async IO
- 同步IO: CPU执行代码的速度极快，遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作 .  
- 多线程和多进程：是解决CPU高速执行能力和IO设备的龟速严重不匹配的一种方法  
- 异步IO：当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。  

## 1. 协程
- 执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。  
- 协程在一个线程执行。协程极高的执行效率，没有线程切换的开销。
- 不需要多线程的锁机制
- 多进程+协程：既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
- generator， yield

## 2. asyncio标准库
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。  
- asyncio提供了完善的异步IO支持；
- 异步操作需要在coroutine中通过yield from完成；
- 多个coroutine可以封装成一组Task然后并发执行。


        import asyncio
        
        @asyncio.coroutine
        def wget(host):
            print('wget %s...' % host)
            connect = asyncio.open_connection(host, 80)
            reader, writer = yield from connect
            header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
            writer.write(header.encode('utf-8'))
            yield from writer.drain()
            while True:
                line = yield from reader.readline()
                if line == b'\r\n':
                    break
                print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
            # Ignore the body, close the socket
            writer.close()
        
        loop = asyncio.get_event_loop()
        tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

## 3. async/await
async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换。  
- 把@asyncio.coroutine替换为async；
- 把yield from替换为await。


        async def hello():
            print("Hello world!")
            r = await asyncio.sleep(1)
            print("Hello again!")

## 4. aiohttp模块
- 把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
- aiohttp则是基于asyncio实现的HTTP框架。