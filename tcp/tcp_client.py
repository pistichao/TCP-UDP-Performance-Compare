import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"


def send(id=0):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server
    s.connect((TCP_IP, TCP_PORT))
    s.send(f"{id}:{MESSAGE}".encode())
    data = s.recv(BUFFER_SIZE)
    s.close()
    print("received data:", data.decode())


def get_client_id():
    id = input("Enter client id:")
    return id


if __name__ == "__main__":
    send(get_client_id())
