import socket
def send_msg():
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    # upd_socket.bind(('', 8080))
    while True:
        send_data = input('请输入想要发送的信息：\n')
        if send_data == 'exit':
            break
        # 发送数据，如果没有绑定本地信息，首次发送系统随机赋予一个本地端口值
        upd_socket.sendto(send_data.encode('utf-8'), ('192.168.16.104',8080))
    upd_socket.close()

def get_msg():
    # 创建套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    localaddr = ('', 7788)
    upd_socket.bind(localaddr)
    # 接收数据
    recv_data = upd_socket.recvfrom(1024)
    recv_msg = recv_data[0]
    send_addr = recv_data[1]
    # 打印收到的信息
    print(f'{str(send_addr)} : {recv_msg.decode("utf-8")}')
    upd_socket.close()

def main():
    send_msg()
    # get_msg()

if __name__ == "__main__":
    main()