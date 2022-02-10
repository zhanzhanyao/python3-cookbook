# Web 开发  
在BS架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。
浏览器只需要请求服务器，获取Web页面，并把Web页面展示给用户即可。

## 1. HTTP协议  

在web应用中，服务器将网页的HTML代码发送给浏览器，由浏览器显示。
服务器与浏览器之间的传输协议是HTTP.
### HTTP请求  
- 浏览器向服务器发送http请求  
包括：方法(Get,Post)，路径，域名，Header，Body(Post)
- 服务器向浏览器返回HTTP响应
包括：响应代码，响应类型，Header，Body
- 若浏览器还需继续向服务器请求其他资源，就再次发出请求

## 2. WSGI接口
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

## 3. 使用web框架  
Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
在WSGI的上进一步抽象，专注于用一个函数处理一个URL。
URL到函数的映射由Web框架完成。

### 流行的web框架--Flask

        pip install flask

        # app.py
        from flask import Flask
        from flask import request
        
        app = Flask(__name__)
        
        
        @app.route("/", methods=["GET", "POST"])
        def home():
            return "<h1>home</h1>"
        
        
        @app.route("/signin", methods=["GET"])
        def signin_form():
            return """<form action="/signin" method="post">
                      <p><input name="username"></p>
                      <p><input name="password" type="password"></p>
                      <p><button type="submit">Sign In</button></p>
                      </form>"""
        
        
        @app.route("/signin", methods=["POST"])
        def signin():
            if request.form["username"] == "admin" and request.form["password"] == "password":
                return "<h3>Hello, admin!</h3>"
        
        if __name__ == "__main__":
            app.run()

        # http://localhost:5000        
        # http://localhost:5000/signin

### Python web框架
- Django: 全能型web框架
- web.py: 小巧的Web框架
- Bottle: 类似Flask
- Rornado: Facebook的开源异步Web框架   

有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数。
  
## 4. 使用模板
MVC：Model-View-Controller