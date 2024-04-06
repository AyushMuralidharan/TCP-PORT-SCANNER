import ssl
import socket

# Function to handle incoming SSL connections
def handle_ssl_connection(connection, address):
    print("Connection from:", address)
    while True:
        data = connection.recv(1024).decode()
        if not data:
            print("Empty the list")
            break
        print("Received from client:", data)
        open_ports = data.split(',')  
        print("Open ports received from client:")
        for i in open_ports:
            print("Port: ",i)

        response = "Received {} open ports from client".format(len(open_ports))
        connection.sendall(response.encode()) 
    connection.close()

# Define server IP address and port
server_ip = "192.168.206.74"
server_port = 8080

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=r"/Users/ayushmuralidharan/Desktop/CNMINI/server.crt", keyfile=r"/Users/ayushmuralidharan/Desktop/CNMINI/server.key")
server_ssl_socket = ssl_context.wrap_socket(server_socket, server_side=True)

server_ssl_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_ssl_socket.listen(5)

print("Server is listening on", server_ip, "port", server_port)

while True:
    # Accept incoming connection
    client_ssl_socket, address = server_ssl_socket.accept()
    handle_ssl_connection(client_ssl_socket, address)