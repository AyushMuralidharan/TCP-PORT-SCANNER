import socket
import ssl

# Function to scan ports on a target IP address
def scan_ports(target_ip, port_start, port_stop):
    open_ports = []
    for port in range(port_start, port_stop + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target_ip, port))
        s.close()
        if result == 0:
            open_ports.append(port)
    return open_ports

# Function to send message to server and receive response
def send_message_to_server(message):
    # Define server IP address and port
    server_ip = "192.168.206.1"
    server_port = 12345

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    ssl_socket = ssl_context.wrap_socket(client_socket)

    # Connect to the server
    ssl_socket.connect((server_ip, server_port))

    # Send message to server
    ssl_socket.sendall(message.encode())

    # Receive response from server
    response = ssl_socket.recv(1024).decode()
    print("Server response:", response)

    # Close the connection
    ssl_socket.close()

# Main function
def main():
    # Prompt user for IP address and port range
    target_ip = input("Enter target IP address: ")
    port_start = int(input("Enter starting port number: "))
    port_stop = int(input("Enter ending port number: "))
    # Scan ports on the target IP address
    open_ports = scan_ports(target_ip, port_start, port_stop)
    # Convert open ports list to string
    open_ports_str = ','.join(map(str, open_ports))
    # Send open ports list to server
    send_message_to_server(open_ports_str)

if __name__ == "__main__":
    main()