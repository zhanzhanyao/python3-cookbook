# Network
- 网络编程就是如何在程序中实现两台计算机的通信。更确切地说，网络通信是两台计算机上的两个进程之间的通信。  
- 比如，浏览器进程和新浪服务器上的某个Web服务进程在通信，而QQ进程是和腾讯的某个服务器上的某个进程在通信。  
- 用Python进行网络编程，就是在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信。  

## 1. TCP/IP协议  
- 互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议。  
- 互联网上每个计算机的唯一标识就是IP地址。如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，所以，IP地址对应的实际上是计算机的网络接口，通常是网卡。  

### IPv4/IPv6
- IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。  
- IPv4
- IPv6: IPv4的升级版
### TCP
- TCP: 建立在IP协议之上的。
- TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
- TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。  
- 许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。  
### TCP报文 
- 包含要传输的数据，还包含源IP地址和目标IP地址，源端口和目标端口。
- 端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。  
- 一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。  


## 2. TCP编程
- 一个Socket表示”打开了一个网络链接“。 打开一个Socket需要知道：目标计算机的IP地址和端口号，并指定协议类型。  
- 创建TCP连接时，发起连接的叫客户端， 响应连接的叫服务器   
  
### 客户端
创建一个基于TCP连接的Socket  

        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
        s.connect(("www.sina.com.cn", 80))
        # 发送数据
        s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

        # 接收数据:
        buffer = []
        while True:
            # 每次最多接收1k字节:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
        data = b''.join(buffer)

        # 关闭连接:
        s.close()

### 服务器  
- 服务器进程首先要绑定一个端口并监听来自其他客户端的连接  
- 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接  
- 服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接  
- 服务器会有大量来自客户端的连接， 服务器要能够区分一个Socket连接是和哪个客户端绑定的。  
- 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。  

        # 服务器程序
        # 创建一个基于IPv4和TCP协议的Socket  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        # 监听端口:
        s.bind(('127.0.0.1', 9999))
        s.listen(5)
        print('Waiting for connection...')
        while True:
            # 接受一个新连接:
            sock, addr = s.accept()
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=tcplink, args=(sock, addr))
            t.start()
        
        
        def tcplink(sock, addr):
            print('Accept new connection from %s:%s...' % addr)
            sock.send(b'Welcome!')
            while True:
                data = sock.recv(1024)
                time.sleep(1)
                if not data or data.decode('utf-8') == 'exit':
                    break
                sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
            sock.close()
            print('Connection from %s:%s closed.' % addr)

## 3. UDP编程
- 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了  
