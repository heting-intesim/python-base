import socket
import threading

# 定义函数：对新的套接字接受和发送消息，并且循环直到客户端停止时关闭与该套接字连接
def new_server(new_socket, ip_port):
    try:
        while True:
            # 接受数据
            recv_data = new_socket.recv(1024)
            if recv_data:
                recv_content = recv_data.decode('utf-8')
                print(f'收到来自 {ip_port} 的消息：{recv_content}')

                # 发送数据
                send_content = '哈哈'
                send_data = send_content.encode('utf-8')
                new_socket.send(send_data)
            else:
                print(f'{ip_port}已关闭！！！')
                break
    except Exception as e:
        print(e)
    finally:
        new_socket.close()

def main():
    # 创建服务端套接字并端口复用
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定IP和端口
    server_socket.bind(('',9999))

    # 监听消息
    server_socket.listen(128)

    # 设置多线程
    while True:

        # 生成新的套接字，一直阻塞直到接收发送的请求
        new_socket, ip_port = server_socket.accept()
        print(f'与客户端{ip_port}建立连接成功！！！')

        # 创建子线程对象并设置为守护主线程
        sub_thread = threading.Thread(target=new_server, args=(new_socket, ip_port), daemon=True)
        # 启动子线程
        sub_thread.start()

    # 关闭被动套接字
    server_socket.close()

if __name__ == "__main__":
    main()