import socket, os, threading
def send_msg(upd_socket, my_name, to_port):
    # 发送数据
    while True:
        send_data = input(f'{my_name}({os.getppid()})：')
        send_data = my_name + ":" + send_data
        if send_data == 'exit':
            break
        upd_socket.sendto(send_data.encode('utf-8'), ('192.168.16.104',to_port))
    upd_socket.close()

def get_msg(upd_socket):
    # 接收数据
    while True:
        recv_data = upd_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        
        # 打印收到的信息
        # print(f'\n{str(send_addr)} : {recv_msg.decode("utf-8")}')
        print(f'\r{recv_msg.decode("utf-8")}')
    upd_socket.close()

def main():
    my_name = input('请输入自己的昵称：')
    my_port = int(input('输入自己的端口号：'))
    to_port = int(input('输入对方的端口号：'))
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    upd_socket.bind(('',my_port)) # 绑定自己端口号
    t_get = threading.Thread(target=get_msg, args=(upd_socket,))
    t_send = threading.Thread(target=send_msg, args=(upd_socket, my_name, to_port))
    t_get.start()
    t_send.start()
    t_get.join()
    t_send.join()

if __name__ == "__main__":
    main()