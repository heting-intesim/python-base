import socket

def tcp_client():
    # 创建套接字
    tcp_client_socket = socket.socket()
    # 建立连接
    tcp_client_socket.connect(('192.168.31.68', 7788))
    # 发送数据
    tcp_client_socket.send('幸福是什么？'.encode('utf-8'))
    data = tcp_client_socket.recv(1024)
    print(data.decode())
    tcp_client_socket.close()

if __name__ == "__main__":
    tcp_client()