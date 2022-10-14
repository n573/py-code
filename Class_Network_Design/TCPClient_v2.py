import socket

# Global Variables
s = None
host = None
port = None


class mySocketError(Exception):
    pass


# Create Socket
def socket_create():
    global host
    global port
    global s
    host = "localhost"
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        raise mySocketError("Socket creation error...")


def socket_connect():
    global host
    global port
    global s

    try:
        s.connect((host, port))
        print("Connected to server -> IP: " + host + " | Port: " + str(port))

    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket connection error...")


# TCP Client Protocol
def tcp_client():
    global host
    global port
    global s

    while True:
        message = input("Message: ")
        if message == "quit":
            break
        else:
            try:
                # created socket
                socket_create()
                # connect to socket
                socket_connect()

                s.sendto(message.encode('utf-8'), (host, port))

                data, addr = s.recv(2048)
                print("IP: " + str(addr[0]) + " | Port: " + (addr[1]))
                print("Message: " + str(data.decode('utf-8')))

            except socket.error as msg:
                print(str(msg))
                raise mySocketError("Socket protocol error...")

    try:
        s.close()
    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket closing error...")


# Main Function
if __name__ == "__main__":

    try:

        # tcp client
        tcp_client()
    except mySocketError as msg:
        print(str(msg))
