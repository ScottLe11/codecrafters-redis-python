import socket  # noqa: F401
import threading


def handle_cilent(client_socket):
    try:
        while(True):
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(b"+PONG\r\n")
    finally:
        client_socket.close()

    

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment the code below to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    # return connection and tuple of client's address (ip, port num)
    
    while True:
        client_socket, address = server_socket.accept() # wait for new client
        client_thread = threading.Thread(target = handle_cilent, args=(client_socket,))
        client_thread.start()
        # data = connection.recv(1024)
        # if not data:
        #     break

        # connection.sendall(b"+PONG\r\n")




if __name__ == "__main__":
    main()
