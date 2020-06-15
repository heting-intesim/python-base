from wsgiref.simple_server import make_server

def app(env, make_reponse):
    #处理业务最核心的函数
    '''
    请求路径：PATH_INFO,
    请求方法：REQUEST_METHOD
    请求查询参数：QUERY_STRING
    客户端的地址：REMOTE_ADDR
    请求上传的数据类型：CONTENT_TYPE
    客户端的代理（浏览器）:HTTP_USER_AGENT
    读取请求上传的字节数据对象：wsgi.input
    wsgi是否使用了多线程:wsgi.multithread:True
    wsgi是否使用了多进程：wsgi.multiprocess:False
    '''
    # for k,v in env.items(): # 打印所有的环境变量
    #     print(k,':',v)
    # 生成响应的对象
    make_reponse('200 OK',[('Content-Type','text/html;charset=utf-8')]) #响应头
    return ['<h3>Hello WSGI</h3>'.encode('utf-8')]  # 返回 响应数据

# 生成web应用服务进程
host = 'localhost'
port = 8000
httpd = make_server(host,port,app)
print(f'running http://{host}:{port}')
# 启动服务，开始监听客户端连接
httpd.serve_forever(poll_interval=0.5)