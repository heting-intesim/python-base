import socket
def send_msg():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_data = input('请输入想要发送的信息：\n')
        if send_data == 'exit':
            break
        s.sendto(send_data.encode('utf-8'), ('192.168.31.93',8080))
    s.close()

def get_msg():
    # 创建套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    localaddr = ('', 8080)
    upd_socket.bind(localaddr)
    # 接收数据
    while True:
        recv_data = upd_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        # 打印收到的信息
        print(f'{str(send_addr)} : {recv_msg.decode("utf-8")}')
    upd_socket.close()

def main():
    get_msg()

if __name__ == "__main__":
    main()