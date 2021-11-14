import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Used while testing to set the local device as the source of all connections
server_socket.bind(('localhost', 3000))
# Allows for any machine to connect to the server
# server_socket.bind((socket.gethostname(), 3000))

# listens out for new connections
server_socket.listen()

# creates a list of currently connected clients
socket_list = [server_socket]
clients = {}


# reads messages from the client
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(10)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False


# continually checks for new connections and new messages
while True:
    read_sockets, _, exception_socket = select.select(socket_list, [], socket_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue
            socket_list.append(client_socket)
            clients[client_socket] = user
            print(
                f"New connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f"New message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            # sends received message to all other users
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # if a client causes an error, disconnect the client
    for notified_socket in exception_socket:
        socket_list.remove(notified_socket)
        del clients[notified_socket]
