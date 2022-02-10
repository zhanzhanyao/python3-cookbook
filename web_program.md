# Web 开发  
在BS架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。
浏览器只需要请求服务器，获取Web页面，并把Web页面展示给用户即可。

## HTTP协议  

在web应用中，服务器将网页的HTML代码发送给浏览器，由浏览器显示。
服务器与浏览器之间的传输协议是HTTP.
### HTTP请求  
- 浏览器向服务器发送http请求  
包括：方法(Get,Post)，路径，域名，Header，Body(Post)
- 服务器向浏览器返回HTTP响应
包括：响应代码，响应类型，Header，Body
- 若浏览器还需继续向服务器请求其他资源，就再次发出请求

## WSGI接口
Web Server Gateway Interface

        # 符合WSGI标准的一个HTTP处理函数，处理http请求
        def application(environ, start_response):
            start_response('200 OK', [('Content-Type', 'text/html')])
            body = "<h1>hello, {}</h1>".format(environ["PATH_INFO"][1:])
            return [body.encode("utf-8")]

        # application()函数必须由WSGI服务器来调用
        from wsgiref.simple_server import make_server
        from hello import application
        # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
        httpd = make_server('', 8000, application)
        print('Serving HTTP on port 8000...')
        # 开始监听HTTP请求:
        httpd.serve_forever()