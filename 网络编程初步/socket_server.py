import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    
    # 等待客户端连接
    s.listen(5)
    while True:
        c, addr = s.accept() # 建立客户端连接
        print('连接地址：', addr)
        c.send('欢迎访问 我的服务器！'.encode('utf-8'))
        c.close()

if __name__ == "__main__":
    main()