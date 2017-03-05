# 将已有的文件描述符包装为文件对象
from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_socket, addr):
    print('Got connection from ', addr)

    client_in = open(client_socket.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_socket.fileno(), 'wt', encoding='latin-1', closefd=False)

    for line in client_in:
        client_out.write(line)
        client_out.flush()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = socket.accept()
        echo_client(client, addr)
