import logging
import socket
import time

logging.basicConfig(level=logging.INFO,
                    filename='tcp_client_out.txt',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"


def send(cid='unknown'):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server
    s.connect((TCP_IP, TCP_PORT))
    for i in range(10):
        s.send(f"{cid}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print(f"received data:{data.decode()}")
        logging.info(f"received data:{data.decode()}")
        time.sleep(1)
    s.close()


def get_client_id():
    cid = input("Enter client id:")
    return cid


if __name__ == "__main__":
    send(get_client_id())
